# Using Python: 

import xml.etree.ElementTree as ET

xml_string = "<employee name="John" id="123" position="Manager" dept="Sales" />"

# Parse the XML
root = ET.fromstring(xml_string)

# Iterate through the child nodes
for child in root:
    # Print all the attributes
    for (name, value) in child.attrib.items():
         print(name + ": " + value)
         
# Output: 
# name: John
# id: 123
# position: Manager
# dept: Sales