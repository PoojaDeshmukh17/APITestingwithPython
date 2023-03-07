import json

exampleJSON = (
    '{"test1":[{"lang1": "Java", "lang2": "Python", "other":["fortran", "go", "C"]}]}')

data = json.loads(exampleJSON)

print(data["test1"][0]["other"][1])
