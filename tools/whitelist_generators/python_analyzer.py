import ast
import json
import sys

class XMLWhitelistAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.tags = set()
        self.attributes = set()

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute):
            func_name = node.func.attr

            # Handle Element and SubElement tag names (2nd arg if SubElement)
            if func_name in {"Element", "SubElement"}:
                # ET.Element('tag')
                if func_name == "Element" and len(node.args) >= 1:
                    tag_node = node.args[0]
                # ET.SubElement(parent, 'tag')
                elif func_name == "SubElement" and len(node.args) >= 2:
                    tag_node = node.args[1]
                else:
                    tag_node = None

                if isinstance(tag_node, ast.Constant) and isinstance(tag_node.value, str):
                    self.tags.add(tag_node.value)

            # Handle .set('attr', 'value')
            elif func_name == "set" and len(node.args) >= 1:
                attr_node = node.args[0]
                if isinstance(attr_node, ast.Constant) and isinstance(attr_node.value, str):
                    self.attributes.add(attr_node.value)

        self.generic_visit(node)

def analyze_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=file_path)

    analyzer = XMLWhitelistAnalyzer()
    analyzer.visit(tree)

    result = {
        "allowed_tags": sorted(analyzer.tags),
        "allowed_attributes": sorted(analyzer.attributes),
        "allowed_entities": []
    }

    with open("whitelists/python_whitelist.json", "w", encoding="utf-8") as out_file:
        json.dump(result, out_file, indent=2)
        print("Whitelist written to python_whitelist.json")

if __name__ == "__main__":
    analyze_file(sys.argv[1])
