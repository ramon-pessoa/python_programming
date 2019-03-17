import xml.etree.ElementTree as ET

tree = ET.parse('items.xml')  
root = tree.getroot()

# removing all sub-elements of an element
root[0].clear()

# create a new XML file with the results
tree.write('newitems5.xml') 