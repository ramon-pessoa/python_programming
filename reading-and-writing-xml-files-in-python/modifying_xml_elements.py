import xml.etree.ElementTree as ET

tree = ET.parse('items.xml')  
root = tree.getroot()

# changing a field text
for elem in root.iter('item'):  
    elem.text = 'new text'

# modifying an attribute
for elem in root.iter('item'):  
    elem.set('name', 'newitem')

# adding an attribute
for elem in root.iter('item'):  
    elem.set('name2', 'newitem2')

tree.write('newitems.xml')