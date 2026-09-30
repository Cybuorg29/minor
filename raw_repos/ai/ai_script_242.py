import base64 
def decode_base64(encoded_s):
   decoded_s = base64.b64decode(encoded_s).decode('utf-8') 
   return decoded_s