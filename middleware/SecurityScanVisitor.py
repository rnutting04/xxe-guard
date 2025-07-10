import re 
import json
import os
from middleware.XMLParserVisitor import XMLParserVisitor

MAX_ENTITY_COUNT = 100


class SecurityScanVisitor(XMLParserVisitor):
    def __init__(self):
        self.alerts = []
        self.entity_count = 0

        # Load whitelist
        whitelist_path = "whitelists/python_whitelist.json"
        if os.path.exists(whitelist_path):
            with open(whitelist_path, "r", encoding="utf-8") as f:
                whitelist = json.load(f)
                self.allowed_tags = set(whitelist.get("allowed_tags", []))
                self.allowed_attributes = set(whitelist.get("allowed_attributes", []))
                self.allowed_entities = whitelist.get("allowed_entities", {})
        else:
            self.allowed_tags = set()
            self.allowed_attributes = set()
            self.allowed_entities = {}


    def visitEntityDecl(self, ctx):
        self.entity_count += 1
        name = ctx.DTDName().getText()
        value = ctx.DTDSTRING().getText().strip('"').strip("'")

        if self.entity_count > MAX_ENTITY_COUNT:
            self.alerts.append(f"[!] Too many ENTITY declarations: {self.entity_count} (Possible DTD overload)")
            return None

        if ctx.PERCENT():
            self.alerts.append(f"[!] Parameter ENTITY declared: {name}")
        elif name in self.allowed_entities and self.allowed_entities[name] == value:
            self.alerts.append(f"[i] Whitelisted ENTITY: {name}")
        elif re.match(r'(?i)^(file|http|https|ftp|php|jar|gopher|data|expect)://', value):
            self.alerts.append(f"[!] External ENTITY: {name} → {value}")
        elif "&" in value or "%" in value:
            self.alerts.append(f"[!] Recursive or parameter ENTITY: {name} → {value}")
        else:
            self.alerts.append(f"[!] Unknown ENTITY: {name} → {value}")

        return self.visitChildren(ctx)


    def visitElementdecl(self, ctx):
        element_name = ctx.DTDName().getText()
        if element_name not in self.allowed_tags:
            self.alerts.append(f"[!] Unexpected ELEMENT: {element_name}")
        elif "ANY" in ctx.getText():
            self.alerts.append(f"[!] ELEMENT {element_name} uses ANY content model (loose structure)")
        else:
            self.alerts.append(f"[i] Allowed ELEMENT: {element_name} declaration")
        return self.visitChildren(ctx)
