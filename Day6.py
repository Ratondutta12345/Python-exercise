### OBJECT ###
# class car:
#     print("Fast")
# car_1 = car()
# car_2 = car()
# print(car_1)
# print(car_2)


# class car1:
#     brand= "Audi"
#     price = 2000000
# print(car1())

# class car2:
#     brand="BMW"
#     price= 30000000
# print(car2())


# class student:
#     def __init__(self,name,age,course):
#         self.name = name
#         self.age = age
#         self.course = course
# st1 = student("Raton Dutta",21,"CSE")
# st2 = student("Sayan Pal",22,"CSE")
# print(st1.name)
# print(st1.age)
# print(st1.course)
# print(st2.name)
# print(st2.age)
# print(st2.course)


# class laptop:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price
# l1 = laptop("Asus",20000)
# l2 = laptop("dell",30000)
# print(l1.brand)
# print(l1.price)

# print(l2.brand)
# print(l2.price)


# class bank:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.balance = balance
# b1 = bank("Raton",20000)
# b2 = bank("Sayan",10000)
# print(b1.owner)
# print(b1.balance)
# print(b2.owner)
# print(b2.balance)


# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def student_info(self):
#         print("Name : ",self.name)
#         print("Marks : ",self.marks)
#     def add_marks(self,amount):
#         print("Name : ",self.name)
#         print("Marks : ",self.marks+amount)
# s1 = student("Raton Dutta",70)
# s1.student_info()
# s1.add_marks(10)


# Exercises
# 1.  Create a Student class with name and marks.
# class student:
#     name="Raton Dutta"
#     marks = 70
# s1 = student()
# print(s1)

# 2.  Add a method that displays student details.
# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def display_info(self):
#         print("Name : ",self.name)
#         print("Marks : ",self.marks)
# s1 = student("Raton Dutta",70)
# s1.display_info()

# 3. Create two Student objects with different values.
# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def display_info(self):
#         print("Name : ",self.name)
#         print("Marks : ",self.marks)
# s1 = student("Raton Dutta",70)
# s2 = student("Sayan Pal",60)
# s1.display_info()
# s2.display_info()

# 4.  Create a Vehicle class and a Car subclass.
# class vehicle:
#     print("I am vehicle")
# class car(vehicle):
#     print("I am car also")
# c1 = car()
# print(c1)