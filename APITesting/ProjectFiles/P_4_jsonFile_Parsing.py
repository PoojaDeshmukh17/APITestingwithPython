# Convert json file into python dictionary ->
# parse content in the json file

import json

from os.path import dirname, join

project_root = dirname(dirname(__file__))

json1_output_path = join(project_root, ("APITestingwithPython\\ResourceFiles\\JsonFiles\\Sample.json"))
print(json1_output_path)

# load()-> For file object we used load method
#          Load method read all the content access by the object(f)


with open(json1_output_path) as f:
    json1data = json.load(f)
    print(json1data)
    print(type(json1data))

    # print second title using index value:
    #   1) Here we pass index value[1] to get the second title
    print(json1data['courses'][1]['title'])  # Cypress
    print(json1data['courses'][0]['price'])  # 50

    # Print website name:
    print(json1data['dashboard']['website'])

    # get the price of "RPA" using title ->
    print(type(json1data['courses']))
    for course in json1data['courses']:
        #        print(course)
        if course['title'] == "RPA":
            print(course['price'])
            assert course['price'] == 45

# Compare two json schemas using python dictionaries:
# How to compare two json schemas->  To compare two json we need to give path of two files and compare them.

json1_output_path = join(project_root, ("APITestingwithPython\\ResourceFiles\\JsonFiles\\Sample1.json"))
# print(json1_output_path)

with open(json1_output_path) as fi:
    json2data = json.load(fi)
    print(json1data == json2data)
    assert json1data == json2data