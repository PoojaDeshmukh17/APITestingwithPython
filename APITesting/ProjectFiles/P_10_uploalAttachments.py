# Sending Attachments through Post request call using Files Dictionary object:

import requests

url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
file = {'file': open('C:\\Users\\GS2534\\Desktop\\Driver\\Test.png','rb')}

Img = requests.post(url,files=file)
print(Img.status_code)
print(Img.text)