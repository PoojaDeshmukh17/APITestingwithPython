import requests


from APITesting.ResourceFiles.AuthConfiguration import *

se = requests.session()
se.auth = auth = ('pooja.deshmukh.gs@gmail.com', getPassword())

url = "https://api.github.com/user"
github_response = requests.get(url,auth=('pooja.deshmukh.gs@gmail.com','SoftwareTester123$'))

print(github_response.status_code)

# when there is a SSL certification we need to use verify=false


# This url gives u the info about the user who logged in:
url2 = "https://api.github.com/user/repos"
response = se.get(url2)
print(response)

# If there is more api , if we want to use more api then we used url globally then we have used session manager
# session(): This method used to create session
# auth :
# session.get (): it has knowledge of authentication as well