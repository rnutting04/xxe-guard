"""Generates sample XML and includes mock entity declarations in comments."""

import xml.etree.ElementTree as ET

# Sample inline ENTITY declarations (simulate hardcoded DTD values)
# <!ENTITY company "Solar Gators">
# <!ENTITY logo "https://example.com/logo.svg">
# <!ENTITY copyright "© 2025 Solar Gators">

def generate_xml():
    """Generate a sample catalog XML with nested elements and attributes."""
    catalog = ET.Element('catalog')

    book = ET.SubElement(catalog, 'book')
    book.set('id', 'bk101')
    book.set('genre', 'Computer')

    author = ET.SubElement(book, 'author')
    author.text = 'Gambardella, Matthew'

    title = ET.SubElement(book, 'title')
    title.text = "XML Developer's Guide"

    publisher = ET.SubElement(book, 'publisher')
    publisher.text = "Solar Gators Publishing"

    logo = ET.SubElement(book, 'logo')
    logo.text = "https://example.com/logo.svg"

    # Another book entry
    book2 = ET.SubElement(catalog, 'book')
    book2.set('id', 'bk102')

    author2 = ET.SubElement(book2, 'author')
    author2.text = 'Doe, Jane'

    title2 = ET.SubElement(book2, 'title')
    title2.text = "Advanced XML Techniques"

    tree = ET.ElementTree(catalog)
    tree.write('output.xml')

if __name__ == "__main__":
    generate_xml()
