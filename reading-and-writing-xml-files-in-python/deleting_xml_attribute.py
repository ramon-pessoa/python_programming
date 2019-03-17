import xml.etree.ElementTree as ET

tree = ET.parse('items.xml')  
root = tree.getroot()

# removing an attribute
root[0][0].attrib.pop('name', None)

# create a new XML file with the results
tree.write('newitems3.xml')  