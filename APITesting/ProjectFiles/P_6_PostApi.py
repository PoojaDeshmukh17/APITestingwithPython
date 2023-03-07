# Understand automating Post http request with Payload and headers

import requests
# request: we used requests library to automate api testing in python.

# Add book:
addBook_response = requests.post('http://216.10.245.166/Library/Addbook.php',
              json={

"name":"Learn Appium Automation with Java",
"isbn":"bfg1rcdd",
"aisle":"2146527",
"author":"John foe"
}, headers={"Content-Type":"application/json"},)

# To convert the response into json format we used json():
print(addBook_response.json())
json_response = addBook_response.json()
print(type(json_response))
# To ignore error press alt+enter

bookID = json_response['ID']
print(bookID)

# # # Delete the book:
response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={

"ID": bookID

},headers={"Content-Type":"application/json"},)

assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()

print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"


