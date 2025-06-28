XML Security Middleware 🔐
Advanced Grammar-Aware XXE Detection and Mitigation Tool

This middleware acts as a language-agnostic XML sanitization layer that pre-parses uploaded XML using ANTLR and applies configurable security rules before passing input to the backend application. It is designed to detect and prevent XML External Entity (XXE) attacks and other DTD-based exploits with greater flexibility than traditional parser configurations.

🚀 Features
Feature	Status
✅ Pre-parse and scan DTDs	Fully implemented
✅ Detect parameter entities	Fully implemented
✅ Recursive & nested ENTITY detection	Fully implemented
⚠️ Whitelist support	Manual, automatic in progress
⚠️ Trusted vs untrusted context	Partial support
✅ Flexible rule logic	Customizable visitor class
✅ Grammar-based blocking	Malicious XML rejected on parse
⚠️ Adaptability	In progress
⚠️ Automatic whitelist generator	In progress
✅ Language agnostic	Yes — Python-based middleware
✅ Open Source	MIT License
✅ Low integration effort	Easily used as a drop-in pre-parser

Why Use This Middleware?
While most defenses against XXE require disabling core XML features entirely, this tool selectively allows safe input and blocks only dangerous constructs. Unlike tools like defusedxml or OWASP sanitizers, this middleware:

Gives visibility into malicious structure (ENTITY, %, recursion, etc.)

Supports custom policies for specific applications

Is fully grammar-aware and not bound to a single platform or parser

Allows preprocessing XML before your backend sees it

🔍 How It Works
Uses an ANTLR4 grammar for XML + DTDs

Walks the parse tree with a custom SecurityScanVisitor

Flags dangerous patterns:

External entities

Parameter entities (<!ENTITY % ...>)

Recursive expansions

Oversized DTDs

Unsafe content models like ANY

Logs or blocks malicious inputs before parsing by any XML processor

🧪 Example Detection Output
```
[i] DOCTYPE present  
[!] Parameter ENTITY declared: a  
[!] External ENTITY: xxe → file:///etc/passwd  
[!] Too many ENTITY declarations: 123 (Possible DTD overload)  
```
📦 Installation
Clone and install dependencies:

```
git clone https://github.com/yourusername/xml-security-middleware.git
cd xml-security-middleware
pip install -r requirements.txt
```
🧩 Integration
This is designed to be integrated before the main XML parser:

```
from middleware.SecurityScanVisitor import SecurityScanVisitor
from antlr4 import InputStream, CommonTokenStream
from XMLLexer import XMLLexer
from XMLParser import XMLParser

def scan(xml_string):
    stream = InputStream(xml_string)
    lexer = XMLLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = XMLParser(tokens)
    tree = parser.document()

    visitor = SecurityScanVisitor()
    visitor.visit(tree)
    return visitor.alerts
```
🧠 Comparison
Feature	This Middleware	defusedxml	OWASP Sanitizer	Java Config
Pre-parses DTDs	✅	✖	➖	✖
Parameter ENTITY detection	✅	✅	➖	✖
Recursive ENTITY detection	✅	✅	✅	✖
Custom rule logic	✅	✖	✅	✖
Language-agnostic	✅	✖ (Python)	➖	✖ (Java)

🏗 Roadmap
 Fully trusted/untrusted context tracking

 Automatic whitelist generator from safe corpus

 Configurable rule profile system

 JSON output mode

 Grammar enhancements (CDATA/XInclude)

📄 License
MIT License

