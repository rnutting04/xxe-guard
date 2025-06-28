# XML Security Middleware

This project is a **preprocessing middleware for XML security**, designed to detect and block malicious or malformed XML before it reaches the main application parser. It focuses on detecting attacks such as XXE (XML External Entity injection), DTD abuse, and recursive entity expansion, all while offering customizable rule definitions and potential for whitelisting trusted structures.

## Features

- Pre-parses DTDs and intercepts malicious patterns before execution
- Detects and blocks:
  - Parameter ENTITY declarations
  - Recursive or nested ENTITY expansions
  - External ENTITY references (file://, http://, etc.)
- Identifies DTD overloads (Billion Laughs-style DoS)
- Flags unsafe use of `ANY` content model
- Supports customizable rules and alert logic
- Partial context-awareness via trust flags
- Designed to be language-agnostic and embeddable in multiple environments
- Future support planned for:
  - Auto-generated whitelists based on observed safe XML patterns
  - More fine-grained trust management

## Comparison With Existing Tools

| Feature                              | Your Middleware | Java Config | defusedxml | OWASP XML Sanitizer | ModSecurity WAF | Go (encoding/xml) |
|-------------------------------------|------------------|-------------|-------------|----------------------|------------------|--------------------|
| Pre-parse DTDs                      | Yes              | No          | No          | Partial              | No               | No (blocks entirely) |
| Parameter ENTITY Detection          | Yes              | No          | Yes         | Partial              | Yes              | No (blocks entirely) |
| Recursive ENTITY Detection          | Yes              | No          | Yes         | Yes                  | Partial          | No (blocks entirely) |
| Whitelist Support                   | Manual only      | No          | No          | Yes                  | No               | No                 |
| Context Awareness (trusted source)  | Partial          | No          | No          | No                   | No               | No                 |
| Flexible Custom Rules               | Yes              | No          | No          | Yes                  | Partial          | No                 |
| Blocks on Grammar Parse             | Yes              | No          | No          | Partial              | Yes              | Yes                |
| Adaptability                        | In progress      | No          | No          | Partial              | Partial          | No                 |
| Automatic Whitelist                 | In progress      | No          | No          | No                   | No               | No                 |
| Language Agnostic                   | Yes              | No (Java)   | No (Python) | Partial              | Yes              | Yes (Go)           |
| Open Source                         | Yes              | Yes         | Yes         | Yes                  | Yes              | Yes                |
| Integration Effort                  | Low              | Low         | Low         | Medium               | High             | Low                |

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourname/xml-security-middleware.git
   cd xml-security-middleware

    ```
2. (Optional) Create and activate a virtual environment:
    ```python
    python -m venv venv
    source venv/bin/activate  # or .\venv\Scripts\activate on Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
The middleware is built as a visitor over a custom ANTLR XML parser. To use it:
```python
from middleware.SecurityScanVisitor import SecurityScanVisitor
visitor = SecurityScanVisitor()
tree = parser.document()  # Assuming `parser` is from ANTLR's XMLParser
visitor.visit(tree)

for alert in visitor.alerts:
    print(alert)
```

## Roadmap

-Context-aware whitelist automation

-Graph-based recursive expansion depth tracking

-Configurable policy engine for enterprises

-Plugin support for Go, Java, and Node.js bridges