
# API: Application Programming Interface.
#      It acts as a communication protocol or interface between the client and the server
#
# 1) When the user enters the inputs, the front end will capture this data and send it to the API.
#    Whenever is it sent to the API, It sends the information over the HTTP protocol.
# 2) All the information frond-end send to the API using an HTTP request
# 3) once the API gets all the details it will send them to the backend.
# 4) Request  format - json or xml
# 5) Once the validation is success, backend will send the response to the API and API send the HTTP
#    response to the front end

# REST API:
# 1) Easy to build and maintain

# Rules to use Rest API :
# 1) Endpoint/ Base URL: Address where API is hosted on the server

# HTTP methods which are commonly used to communicate with the rest API's is :
# GET, POST, PUT, DELETE (CRUD) Operations:

# 1) GET: The GET method used to extract the information from the given server using a given URL.
#    while using GET request, it should only extract data and should have no other effect on the data
#    (No payload or body required)

# 2) POST: The POST method used to send data to the server. For eg: Customer information, file, upload, using HTML forms

# 3) PUT: replace all current representations of the target resource with the uploaded content

# 4) DELETE: Remove all current representations of the target resource given by a URL


# 1) Resources: Resources represent API/collection which can be accessed from the server
# EX: Google.com/maps    ->  Here maps is resources and Google.com is the base URL


# 2) Path Parameters:
#  Path parameters are variable parts of a UPL path. They are typically used to point to specific resources within a collection, such as a user identified by ID

# EX: https://amamzon.com/orders/112
#     Here 112 -> path parametrs
#               Orders -> Resources
#               https://amamzon.com -> base URL


# 3) Query parameter:
# The query parameter is used to sort/filter the resources.
# Query parameters are identified with ?""

# EX: https://amamzon.com//orders?sort_by=299054
#        Here ?sort_by=299054 -> Query parameter

# requests library : Allow to send/retrive HTTP requests using python