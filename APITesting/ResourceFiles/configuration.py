import configparser
import mysql.connector
from mysql.connector import Error

def getConfig():
    config = configparser.ConfigParser()
    config.read('properties1.ini')
    return config

# # connection utilities of P_11_Mysql ->
# #Create dictionary object:
# connect_config = {
#     'user' : getConfig()['SQL']['user'],
#     'password' : getConfig()['SQL']['password'],
#     'host' : getConfig()['SQL']['host'],
#     'database' :getConfig()['SQL']['database'],
# }
#
# def getConnection():
#     try:
#         connection = mysql.connector.connect(**connect_config)
#         if connection.is_connected():
#             print("Connection Successful")
#             return connection
#     except Error as e:
#         print(e)

