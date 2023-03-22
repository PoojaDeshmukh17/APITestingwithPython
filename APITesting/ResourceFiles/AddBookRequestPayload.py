from APITesting.ResourceFiles.configuration import *

def addBookPayload(isbn):
    body = {

        "name" :"Learn Appium Automation with Java",
        "isbn" : isbn,
        "aisle" :"214527",
        "author" :"John foe"
    }
    return body

def deleteBookPayload(bookID):
    body = {

        "ID": bookID

}
    return body


def buildPayLoadFromDB(query):
# creating a dic and send it to the main test:
    addBody = {}
    tp = getQuery(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody