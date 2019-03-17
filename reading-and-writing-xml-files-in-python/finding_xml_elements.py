import xml.etree.ElementTree as ET  
tree = ET.parse('items.xml')  
root = tree.getroot()

# find the first 'item' object
for elem in root:  
    print(elem.find('item').get('name'))

# find all "item" objects and print their "name" attribute
for elem in root:  
    for subelem in elem.findall('item'):

        # if we don't need to know the name of the attribute(s), get the dict
        print(subelem.attrib)      

        # if we know the name of the attribute, access it directly
        print(subelem.get('name'))