import json
import re 

json_as_string = open('nutrients.json', 'r')
# Call this as a recursive function if your json is highly nested
data = json.load(json_as_string)
print data
