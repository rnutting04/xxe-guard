"""sample xml source file generation for testing python whitelisting"""
import xml.etree.ElementTree as ET

def generate_xml():
    """sample generation of xml file"""
    root = ET.Element('catalog')
    book = ET.SubElement(root, 'book')
    book.set('id', 'bk101')

    author = ET.SubElement(book, 'author')
    author.text = 'Gambardella, Matthew'

    title = ET.SubElement(book, 'title')
    title.text = "XML Developer''s Guide"

    tree = ET.ElementTree(root)
    tree.write('output.xml')
