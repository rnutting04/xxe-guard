import ast
import json
import sys
import re

class XMLWhitelistAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.tags = set()
        self.attributes = set()
        self.entities = dict()

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute):
            func_name = node.func.attr

            # Handle Element and SubElement tag names
            if func_name in {"Element", "SubElement"}:
                tag_node = node.args[0] if func_name == "Element" else node.args[1] if len(node.args) > 1 else None
                if isinstance(tag_node, ast.Constant) and isinstance(tag_node.value, str):
                    self.tags.add(tag_node.value)

            # Handle set("attr", "value")
            elif func_name == "set" and len(node.args) >= 2:
                attr_node, val_node = node.args[0], node.args[1]
                if isinstance(attr_node, ast.Constant) and isinstance(attr_node.value, str):
                    self.attributes.add(attr_node.value)
                if isinstance(val_node, ast.Constant) and isinstance(val_node.value, str):
                    if self._looks_like_entity_value(val_node.value):
                        self.entities[attr_node.value] = val_node.value

        self.generic_visit(node)

    def visit_Assign(self, node):
        if isinstance(node.targets[0], ast.Attribute):
            attr = node.targets[0].attr
            value_node = node.value
            if attr == "text" and isinstance(value_node, ast.Constant) and isinstance(value_node.value, str):
                if self._looks_like_entity_value(value_node.value):
                    # Guess a name from context if possible (not perfect)
                    guessed_name = getattr(node.targets[0].value, "id", None) or "entity_{}".format(len(self.entities))
                    self.entities[guessed_name] = value_node.value

        self.generic_visit(node)

    def _looks_like_entity_value(self, val):
        return re.match(r"^(https?|file|ftp|data|jar|php|expect)://", val) or len(val) < 100


def analyze_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=file_path)

    analyzer = XMLWhitelistAnalyzer()
    analyzer.visit(tree)

    result = {
        "allowed_tags": sorted(analyzer.tags),
        "allowed_attributes": sorted(analyzer.attributes),
        "allowed_entities": analyzer.entities
    }

    with open("whitelists/python_whitelist.json", "w", encoding="utf-8") as out_file:
        json.dump(result, out_file, indent=2)
        print("Whitelist written to python_whitelist.json")

if __name__ == "__main__":
    analyze_file(sys.argv[1])
