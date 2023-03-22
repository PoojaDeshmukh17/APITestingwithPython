from behave import *
import requests
import string
import random


from APITesting.ResourceFiles.configuration import *
from APITesting.ResourceFiles.AddBookRequestPayload import *
from APITesting.ResourceFiles.ApiResources import *


@given('the book details which needs to be added to Library')
def step_impl(context):
    randomStringSize = random.randint(5, 15)
    context.addBookUrl = getConfig()['API']['baseUrl'] + ApiResources.addBook
    # context.addBookUrl = "http://216.10.245.166" + ApiResources.addBook
    context.addBookHeader = {"Content-Type": "application/json"}
    context.payLoad = context.addBookHeader

    # generating random strings
    randomString = ''.join(random.choices(string.ascii_uppercase +
                                          string.digits, k=randomStringSize))


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.addBook_response = requests.post(context.addBookUrl, headers=context.addBookHeader, json=context.payLoad, )

@then('book is successfully added')
def step_impl(context):
    # print(context.addBook_response.json())
    json_response = context.addBook_response.json()
    print(json_response)
    print(type(json_response))
    bookID = json_response['ID']
    print(bookID)
    assert json_response["Msg"] == "successfully added"


@given('The book details which needs to be addd to the library')
def step_implementation(context):
    # Use context to use the variable across methods or files
    context.url = get_config()['API']['endpoint'] + ApiEndpoints.addBook
    context.headers = {'Content-Type': 'application/json'}


@when('AddBook POST API method is executed')
def step_impl(context):
    context.response = requests.post(context.url, json=add_book_payload('zsoqaqarddaqsdess'), headers=context.headers)


@then('Book is successfully added')
def step_impl(context):
    assert context.response.status_code == 200, "Book is successfully added"


@then('The response received should be in the json format')
def json_response(context):
    assert False == True, "2001 The response received should be in the json format"
