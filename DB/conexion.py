import sqlite3
import os
def get_connection():
    path = os.path.abspath(os.getcwd())+'/DB/libros.sqlite3'
    connection = sqlite3.connect(path)
    return connection

