import io
import re
from antlr4 import InputStream, CommonTokenStream
from middleware.XMLLexer import XMLLexer
from middleware.XMLParser import XMLParser
from middleware.SecurityScanVisitor import SecurityScanVisitor
from antlr4.error.ErrorListener import ErrorListener



def run_regex_scan(xml_string):
    patterns = {
        r'<!ENTITY\s+[^>]+SYSTEM': "[!] Detected SYSTEM external ENTITY",
        r'<!ENTITY\s+%[^>]+SYSTEM': "[!] Detected SYSTEM parameter ENTITY",
        r'<!DOCTYPE\s+[^>]+\[': "[!] Detected DOCTYPE with internal subset",
        r'&[a-zA-Z0-9]+;': "[!] Detected general ENTITY reference",
        r'php://': "[!] Detected use of php:// stream",
        r'file://': "[!] Detected use of file://",
        r'ftp://': "[!] Detected use of ftp://",
        r'http[s]?://': "[!] Detected use of http(s)://"
    }

    alerts = []

    for pattern, message in patterns.items():
        if re.search(pattern, xml_string, re.IGNORECASE | re.DOTALL):
            alerts.append(message)

    return alerts

class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax error at line {line}:{column} - {msg}")
        

def secure_parse(xml_string):
    try:
        input_stream = InputStream(xml_string)
        lexer = XMLLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = XMLParser(tokens)

        # Attach strict error listener
        error_listener = ThrowingErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)

        tree = parser.document()
        visitor = SecurityScanVisitor()
        visitor.visit(tree)

        alerts = visitor.alerts
        if not alerts:
            alerts = ["[i] No issues detected by primary parser"]

        return alerts

    except Exception as e:
        print("[!] ANTLR parser failed:", e)
        print("[*] Falling back to regex/static scan...")

        fallback_alerts = run_regex_scan(xml_string)
        if not fallback_alerts:
            fallback_alerts = ["[i] No issues detected by fallback scan"]
        return fallback_alerts
