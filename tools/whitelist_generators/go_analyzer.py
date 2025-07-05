import os
import json
import re

def extract_xml_tags_from_structs(content):
    tag_pattern = re.compile(r'`[^`]*xml:"([^", ]+)')
    return tag_pattern.findall(content)

def extract_xml_calls(content):
    call_pattern = re.compile(r'\bxml\.(Marshal|Unmarshal)\b')
    return bool(call_pattern.search(content))

def analyze_go_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not extract_xml_calls(content):
        return None  # Not an XML-related file

    tags = extract_xml_tags_from_structs(content)
    return tags

def walk_directory(root_dir):
    whitelist = {
        "elements": [],
        "attributes": []
    }

    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".go"):
                full_path = os.path.join(subdir, file)
                tags = analyze_go_file(full_path)
                if tags:
                    whitelist["elements"].extend(tags)

    # Remove duplicates
    whitelist["elements"] = sorted(set(whitelist["elements"]))
    return whitelist

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Go XML Analyzer")
    parser.add_argument("directory", help="Path to Go source directory")
    parser.add_argument("--output", default="whitelist.json", help="Output JSON whitelist file")

    args = parser.parse_args()
    whitelist = walk_directory(args.directory)

    with open(args.output, "w") as f:
        json.dump(whitelist, f, indent=2)

    print(f"[+] Whitelist saved to {args.output}")

