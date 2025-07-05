import re 
from XMLParserVisitor import XMLParserVisitor

MAX_ENTITY_COUNT = 100

class SecurityScanVisitor(XMLParserVisitor):
    def __init__(self):
        self.alerts = []
        self.entity_count = 0

    def visitDoctypedecl(self, ctx):
        self.alerts.append("[i] DOCTYPE present")
        if ctx.externalID():
            ext_value = ctx.externalID().getText()
            self.alerts.append(f"[!] DOCTYPE uses external DTD reference → {ext_value}")
        return self.visitChildren(ctx)

    def visitEntityDecl(self, ctx):
        self.entity_count += 1
        name = ctx.DTDName().getText()
        value = ctx.DTDSTRING().getText().strip('"').strip("'")

        if self.entity_count > MAX_ENTITY_COUNT:
            self.alerts.append(f"[!] Too many ENTITY declarations: {self.entity_count} (Possible DTD overload)")
            return None

        if ctx.PERCENT():
            self.alerts.append(f"[!] Parameter ENTITY declared: {name}")
        elif re.match(r'(?i)^(file|http|https|ftp|php|jar|gopher|data|expect)://', value):
            self.alerts.append(f"[!] External ENTITY: {name} → {value}")
        elif "&" in value or "%" in value:
            self.alerts.append(f"[!] Recursive or parameter ENTITY: {name} → {value}")
        else:
            self.alerts.append(f"[i] Safe ENTITY: {name}")

        return self.visitChildren(ctx)

    def visitElementdecl(self, ctx): 
        element_name = ctx.DTDName().getText()
        if "ANY" in ctx.getText():
            self.alerts.append(f"[!] ELEMENT {element_name} uses ANY content model (loose structure)")
        else:
            self.alerts.append(f"[i] ELEMENT {element_name} declaration")
        return self.visitChildren(ctx)
