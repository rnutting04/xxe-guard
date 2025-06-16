from antlr4 import InputStream, CommonTokenStream
from middleware.SecurityScanVisitor import SecurityScanVisitor
from middleware.XMLLexer import XMLLexer
from middleware.XMLParser import XMLParser


def run_xxe_check(xml_data: str) -> bool:
    input_stream = InputStream(xml_data)
    lexer = XMLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = XMLParser(stream)

    tree = parser.document()
    scanner = SecurityScanVisitor()
    scanner.visit(tree)

    # Print alerts (optional for debugging)
    for alert in scanner.alerts:
        print(alert)

    # Basic decision logic
    for alert in scanner.alerts:
        if "[!]" in alert:
            return True  # Block if any critical issues were found

    return False

