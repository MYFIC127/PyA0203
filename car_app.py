#-----------< V.0.1.0 >-----------
from typing import Any
#TODO: 

class Car:
    '''Car class to describes a 4 wheeled car'''
    wheels = 4          #class attribute
    def __init__(self, maker, model, year, price, color="white"):
        self.maker = maker          #instance attribute
        self.model = model
        self.year = year
        self.price = price
        self.color = color
        self.checkup = []

    def add_checkup(self, date):        #instance method
        self.checkup.append(date)

    def leased(self, months):
        if months <= 12:
            instalment = int(self.price * 1.05 / months)
        else :
            instalment = int(self.price * 1.1 / months)
        return instalment

    def __str__(self) -> str:
        return f"{self.maker}-{self.model}"

    # def __del__(self):
    #     print("Goodbye!")

    def __repr__(self) -> str:
        return "Car Class"

    def __len__(self) -> int:
        return len(self.checkup)
    
    def __getitem__(self,index):
        return self.checkup[index]
    
    def __setitem__(self, index, value) -> None:
        self.checkup.insert(index,value)

    def __call__(self, color) -> Any:
        self.color = color
        print(f"The new color is {self.color}")

    def __add__(self, other):
        return self.price + other.price

    def __radd__(self,other):
        return self.price + other

    def __sub__(first,second):
        return first.price - second.price
    
    def __rsub__(first,second):
        return first.price - second

    def __eq__(first, second):
        if first.maker == second.maker and first.model == second.model and first.year == second.year and first.price == second.price and first.color == second.color:
            return True
        else:
            return False
#----------------< Main >-------------
car1 = Car("Toyota", "Camry", 2022, 32000, "Blue")
car2 = Car("BMW", "518i", 2020, 45000)
car3 = Car("Benz", "69420", 2017, 65001)
car4 = Car("Subaru", "Kyun", 2015, 1003)
# car1.add_checkup("2023/06/08")

# print(car1)             #__str__
# print(repr(car1))       #__repr__
# print(len(car1))        #__len__
# print(car1[0])          #__getitem__
# car1[1] = "2023/10/10"  #__setitem__
# print(car1.checkup)
# car1("Black")           #__call__
# print(car1.color)
# print(car1+car2)        #__add__
# print(car1-car2)        #__sub__
# print(car1==car2)       #__eq__
# print(car1.__doc__)     #__doc__
# print(car1.__dict__)    #__dict__

# print((car1+car2).price)
print(car1-car2-car3-car4-430)