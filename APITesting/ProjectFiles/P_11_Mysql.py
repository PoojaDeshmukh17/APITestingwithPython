# Setup Database and start connection:
# Create Connection utility and pass the SQL connection externally into test :

import mysql.connector
from APITesting.ResourceFiles.configuration import *
# mysql.connector.connect : This method help us to connect to the database.
#                           It has four arguments: ( host, database,user,password)

# connection = mysql.connector.connect(host='localhost', database='PythonAutomation',
#                                      user='root', password='The Summer Is Back !')
connection = getConnection()
print(connection.is_connected())
# is_connected: Return type is boolean
#               True : connected to the database
#               False : Not connected

cursorObj = connection.cursor()

# cursor(): This method form a streamline connection for talk to the database table.
# cursorObj :It is an object that is used to make the connection for executing SQL queries.
#             It acts as a middleware between database and python.
# fetchone() : Fetch only one record from the table         -> Return type: Tuple
# fetchall() : Fetch all record from the table( where the cursor is present)   -> Return type: List of Tuple

cursorObj.execute('SELECT * FROM company.department;')

# row1 = cursorObj.fetchone()
# print(row1)
# print(row1[2])                                     # Japan

rowAll = cursorObj.fetchall()
print(rowAll)
print(rowAll[1])                                     # ('Marketing', 500, 'China')

# Sum of Employee:
sum = 0
for row in rowAll:
    sum = sum + row[1]

print(sum)                                           # 1050
# assert sum == 361

