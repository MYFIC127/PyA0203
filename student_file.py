class Student:
    university = "Tehran"
    def __init__(self, first_name, last_name, age, std_id):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.std_id = std_id
    
    def __del__(self):
        print("ByeBye")



#--------< Main >--------
std1 = Student("Ali", "Ahmadi", 22, 12345)
std2 = Student("Yasin", "Fozi", 19, 41022)
std3 = Student("Aida", "Vajd", 27, 22040)

# print(std1.age)