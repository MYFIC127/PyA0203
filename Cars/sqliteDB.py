#TODO: Random id generator, pandas
import sqlite3
from sys import path

def create_cars_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS cars_table(car_id INTEGER PRIMARY KEY, maker TEXT, model Text, year INTEGER, price FLOAT, color TEXT)")

def new_car(*car):
    try:
        cursor.execute("INSERT INTO cars_table VALUES(?,?,?,?,?,?)",car)
        database.commit()
    except(sqlite3.IntegrityError) :
        print("Car ID must be a unique five digit number")

#-----------------< Main>------------------

database = sqlite3.connect(path[0]+"/cars_db.db")
cursor = database.cursor()

all_cars = list(cursor.execute("SELECT car_id,maker,price FROM cars_table WHERE maker=? ORDER BY price",["Toyota"]))
print(all_cars)