def myfunc(param):
 if not isinstance(param, str):
     print(f"Expected a string for parameter 'param' but received type '{type(param).__name__}'")