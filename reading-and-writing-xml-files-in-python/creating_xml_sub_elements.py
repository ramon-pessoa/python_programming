import xml.etree.ElementTree as ET

tree = ET.parse('items.xml')  
root = tree.getroot()

# adding an element to the root node
attrib = {}  
element = root.makeelement('seconditems', attrib)  
root.append(element)

# adding an element to the seconditem node
attrib = {'name2': 'secondname2'}  
subelement = root[0][1].makeelement('seconditem', attrib)  
ET.SubElement(root[1], 'seconditem', attrib)  
root[1][0].text = 'seconditemabc'

# create a new XML file with the new element
tree.write('newitems2.xml') 