import json  
import xmltodict  

# Load JSON data
data_str = '''
   {  
   "employees":{  
      "employee":[  
         {  
            "name":"John Smith",
            "id":123
         },
         {  
            "name":"Jane Doe",
            "id":456
         }
      ]
   }
} 
'''
data_dict = json.loads(data_str)

# Covert JSON to XML
xml_data = xmltodict.unparse(data_dict, attr_prefix='', cdata=False)
xml_data = xml_data.replace('<employee>', '<employee person="">')

# Print XML
print(xml_data)