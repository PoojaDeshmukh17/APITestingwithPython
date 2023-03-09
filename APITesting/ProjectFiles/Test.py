import requests
import string
import random
import json
import configparser

# configparser: Configparser  used to store the global configuration parameters

from APITesting.ResourceFiles.configuration import *
from APITesting.ResourceFiles.AddBookRequestPayload import *
from APITesting.ResourceFiles.ApiResources import *

# Initializing size of random string
randomStringSize = random.randint(5,15)

# Add book:

addBookUrl = getConfig()['API']['baseUrl'] + ApiResources.addBook
addBookHeader = {"Content-Type":"application/json"}

# generating random strings
randomString = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=randomStringSize))

addBook_response = requests.post(addBookUrl, headers=addBookHeader, json=addBookPayload("Pooja_" + str(randomString)),)

# To convert the response into json format we used json():

json_response = addBook_response.json()
print(json_response)
print(type(json_response))
# To ignore error press alt+enter

bookID = json_response['ID']
print(bookID)

# # Delete the book:
deleteBookUrl = getConfig()['API']['baseUrl'] + ApiResources.deleteBook
deleteBookHeader = {"Content-Type":"application/json"}

deleteBook_response = requests.post(deleteBookUrl, headers=deleteBookHeader, json=deleteBookPayload(bookID),)
deleteBookJsonResponse = deleteBook_response.json()
print(deleteBookJsonResponse)
assert deleteBook_response.status_code == 200
res_json = deleteBook_response.json()

print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"


url = "https://api.github.com/user"
response = requests.get(url,auth=('pooja.deshmukh.gs@gmail.com', 'SoftwareTester123$'))

print(response.status_code)