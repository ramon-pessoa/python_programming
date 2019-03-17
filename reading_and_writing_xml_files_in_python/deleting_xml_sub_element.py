import xml.etree.ElementTree as ET

tree = ET.parse('items.xml')  
root = tree.getroot()

# removing one sub-element
root[0].remove(root[0][0])

# create a new XML file with the results
tree.write('newitems4.xml')  