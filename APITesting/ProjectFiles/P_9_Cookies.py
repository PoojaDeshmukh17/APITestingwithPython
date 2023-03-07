#  How to handle cookies:
#  handle date cookies along with url:

import requests

# visit month:
cookie = {'visit': 'February'}

response = requests.get('http://rahulshettyacademy.com', allow_redirects=False, cookies=cookie, timeout=1)

# Redirection:
# print(response.history)

print(response.status_code)

# create session: If we make session then cookie will apply to every call(we can call session using se.get)

se = requests.session()
se.cookies.update(({'visit-month': 'February'}))

# https://httpbin.org:
response = se.get('https://httpbin.org/cookies',allow_redirects=False,cookies={'visit-year': '2023'}, timeout=1)
print(response.text)

# Note:
# 1.We have to send cookies always in dictionary format.
# 2. allow_redirects=False : It will stop after it's receive 1st status code'
# 3. time out : This will wait sec then it will response back.
# 4.[ 301,200 ]: Any status code start with 300 then its a redirection, we can achieve this using .history