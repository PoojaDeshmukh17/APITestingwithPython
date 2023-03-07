import gmail as gmail
import requests

from APITesting.ProjectFiles.P_8_Authentications import github_response
from APITesting.ResourceFiles.AuthConfiguration import *

url = "https://api.github.com/user"
github_response = requests.get(url,auth=('pooja.deshmukh.gs@gmail.com','SoftwareTester123$'))

print(github_response.status_code)

