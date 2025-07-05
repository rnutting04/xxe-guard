from antlr4 import InputStream 
from XMLLexer import XMLLexer

data = """<?xml version="1.0"?>
<!DOCTYPE note [
  <!ENTITY company "OpenAI">
]>
<note>&company;</note>
"""

lexer = XMLLexer(InputStream(data))
tokens = lexer.getAllTokens()

# Use symbolicNames through the class
symbolic_names = lexer.symbolicNames

for t in tokens:
    print(f"{t.text:35} → {symbolic_names[t.type]}")
