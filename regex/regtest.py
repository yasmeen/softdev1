import re

def find_phone(s):
  expr = "[0-9]{3}-[0-9]{3}-[0-9]{4}"
  result = re.findall(expr, s)
  return result
