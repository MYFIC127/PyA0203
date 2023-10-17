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

def car_information(carid):
    car = cursor.execute("SELECT * FROM cars_table WHERE car_id=?", (carid,)).fetchone()
    if car == None :
        raise ValueError("Car ID not found !")
    #-----Convert-Tuple-To--------
    keys = ("car_id", "maker", "model", "year", "price", "color")
    car_dict = dict(zip (keys,car))
    #-----------------------------
    return car

def maker_information(maker):
    info = list(cursor.execute("SELECT * FROM cars_table WHERE maker=?",(maker,)))
    models = []
    i = 0
    if len(info)==0 :
        raise ValueError("Maker not found !")
    for car in info:
        models += [car[2]]

    return models

def raise_car_price(percent):
    cursor.execute("UPDATE cars_table SET price=price*?",(1 + percent/100,))   
    database.commit()

#-----------------< Main>------------------

database = sqlite3.connect(path[0]+"/cars_db.db")
cursor = database.cursor()

# all_cars = list(cursor.execute("SELECT car_id,maker,price FROM cars_table WHERE maker=? ORDER BY price",["Toyota"]))
# print(car_info(10102))
# print(maker_information("Toyota"))
