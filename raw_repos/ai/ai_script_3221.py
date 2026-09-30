def print_string_keys(json_object):
  for key in json_object:
      if isinstance(json_object[key], str):
          print(key)