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
