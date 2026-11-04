### Function ###
# A function is a reusable block of code that performs a specific task.

# def welcome():
#     print("Welcome to Python!")

# welcome()

# Parameter 
# A parameter allows us to send information into a function.
# def greet(name):
#     print(f"name : {name}")

# greet("Raton Dutta")

# def student_info(name,age):
#     print("Name : ",name)
#     print("Age : ",age)

# student_info("Raton Dutta",21)

# def sum(a,b):
#     return a+b
# result = sum(10,20)
# print(result)

# return 
# def multiply(a,b):
#     return a*b
# result = multiply(10,20)
# print(result)

# def add(a,b):
#     return a+b
# result = add(10,20)
# print(result)


## Default parameter
# A default argument is a value that Python automatically uses if you don't provide an argument.
# def greet(name="Raton Dutta"):
#     print("My name is",name)
# greet("Amit")


# def info(name,age,city):
#     print("Name : ",name)
#     print("Age : ",age)
#     print("City : ",city)
# info(age=21,city="Kolkata",name="Raton")


# Global variable
# A global variable is a variable that is defined outside of a function and can be accessed from anywhere in the code.
# city = "Kolkata"
# def show_city():
#     print("City : ",city)
# show_city()

# def student():
#     name = "Raton Dutta"
#     age = 21
#     print("Name : ",name)
#     print("Age : ",age)
# student()


# # Lamda function
# square = lambda a: a*a
# result = square(5)
# print(result)


# 1. Write a function that returns the square of a number.
# def square(a):
#     return a*a
# result = square(5)
# print(result)


# 2. Write a function that checks whether a number is even.
# number = int(input("Enter a number : "))
# def is_even(number):
#     if(number%2==0):
#         print(f"{number} is a even number.")
#     else:
#         print(f"{number} is a odd number.")
# is_even(number)


# 3. Write a function that returns the largest of three numbers.
# def largest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     else:
#         return c
# largest_number = largest(40,20,30)
# print(largest_number)

# 4. Call the same function with different arguments
# def greet(a,b):
#     print(f"{a} + {b} = {a+b}")
# greet(2,3)
# greet(5,10)
# greet(20,30)