import sqlite3
from sys import path

def create_cars_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS cars_table(maker TEXT, model Text, year INTEGER, price FLOAT, color TEXT)")

#-----------------< Main>------------------

database = sqlite3.connect(path[0]+"/cars_db.db")
cursor = database.cursor()






database.commit()
database.close()