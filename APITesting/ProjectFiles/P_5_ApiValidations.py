#  Get http request calls and get response using Json method
import json

import requests
# requests library : Allow to send/retrieve HTTP requests using python

response = requests.get('http://216.10.245.166/Library/GetBook.php',
                        params={'AuthorName':'APITester'},)

# print(json_response.text)
# print(type(json_response.text))
# dict_response = json.loads(json_response.text)
# print(dict_response)
# print(type(dict_response))

json_response = response.json()
print(type(json_response))
print(json_response[0]['isbn'])

# To print status code
assert response.status_code == 200

# To print all the headers:
# print(response.headers)

# Verify if content type is json or not
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

# json(): This method used to convert json string into list

# Retrieve the book details with ISBN RS423:
for actualBook in json_response:
   #print(actualBook)
    if actualBook['isbn'] == 'dcsrfx':
        print(actualBook)


expectedBook = {
        "book_name": "DummyBook",
        "isbn": "abcd6ef",
        "aisle": "1231"
    }
print(expectedBook)
# assert actualBook == expectedBook