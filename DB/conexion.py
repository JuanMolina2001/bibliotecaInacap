import mysql.connector
def get_connection():
    connection = mysql.connector.connect(host = 'localhost',database = 'biblioteca',user = 'root',password = '')
    return connection
def close_connection(connection):
    if connection:
        connection.close()