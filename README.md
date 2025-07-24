
# XXE Guard

XXE Guard is a language-agnostic XML security middleware that detects and blocks XML External Entity (XXE) attacks using both grammar-based parsing and customizable whitelisting. It is designed to be containerized and easily integrated into existing pipelines or APIs.

## Features

- **ANTLR-based XML parsing**  
  Parses XML with a custom grammar that supports DTDs, internal subsets, parameter entities, and more.

- **SecurityScanVisitor**  
  Walks the parsed XML and flags:
  - External entities (e.g., `file://`, `http://`, `php://`)
  - Recursive or parameter entities
  - Excessive entity declarations (DoS)
  - Use of `ANY` in element declarations
  - Use of external DTDs

- **Static Whitelisting Support**  
  Supports auto-generated JSON whitelists from source code, identifying:
  - Allowed tags
  - Allowed attributes
  - Allowed entity name-value pairs

- **Regex-based Fallback Scanner**  
  If malformed XML causes the primary parser to fail, a regex scanner runs as a fallback.

- **Dockerized API**  
  Runs as a Flask API inside Docker and accepts XML payloads via `/scan-xml`.

## Current API Endpoints

- `GET /`  
  HTML form for manual XML payload submission.

- `POST /scan-xml`  
  Accepts XML payload (raw or via form). Returns alerts or blocks based on findings.

## Example Detection Output

   ```less
    [i] DOCTYPE present  
    [!] Parameter ENTITY declared: a  
    [!] External ENTITY: xxe → file:///etc/passwd  
    [!] Too many ENTITY declarations: 123 (Possible DTD overload)  

   ```

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

## Directory Structure
```bash
xxe-guard/
├── api/
│   └── app.py                  # Flask entry point
├── middleware/
│   ├── parser_wrapper.py       # Secure parsing logic
│   ├── SecurityScanVisitor.py  # Custom visitor
│   ├── XMLLexer.g4             # ANTLR lexer grammar
│   └── XMLParser.g4            # ANTLR parser grammar
├── tools/
│   └── whitelist_generators/   # Source code scanners (e.g., for Python)
├── whitelists/
│   └── python_whitelist.json   # Auto-generated whitelist
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourname/xml-guard.git
   cd xml-guard

    ```
2. Optioanlly, run the whitelist generator:
    ```bash
    python tools/whitelist_generators/python_analyzer.py <path_to_source_code>
    ```

3. Build and run the Docker container:
    ```bash
    docker-compose up --build
    ```

## Roadmap

- Context-aware whitelist automation

- Graph-based recursive expansion depth tracking

- Configurable policy engine for enterprises

