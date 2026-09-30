import xml.etree.ElementTree as ET 

# parse the xml file
root = ET.parse('employees.xml').getroot()
for employee in root.findall('employee'):
    name = employee.find('name').text
    print(name)