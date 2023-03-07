# Convert json strings into python dictionary ->

import json

sample = '{"name": "John", "languages": ["Java", "Python"]}'
# sample variable holds the json file contents.

# Loads(): Loads method allows us to convert a JSON string into a dictionary
#          It will take string as an arguments
dictionary = json.loads(sample)
print(dictionary)
print(type(dictionary))

# get the name:
print(dictionary['name'])                   # John

# get the lang:
print(dictionary['languages'])              # ['Java', 'Python']

# get first lang: we used index value
list_languages = dictionary['languages']
print(type(list_languages))
print(list_languages[0])                    # java
print(list_languages[1])                    # Python