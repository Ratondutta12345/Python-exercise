# # 1. Variables & Input
# name = str(input("Enter your name : "))
# age = int(input("Enter your age : "))
# city = str(input("Enter your city : "))

# print(f"Name : {name}")
# print(f"Age : {age}")
# print(f"City : {city}")


# # 2. Even or Odd
# number = int(input("Enter a number : "))
# if(number%2==0):
#     print("Even number")
# else:
#     print("Odd number")


# # 3. Positive, Negative or Zero
# number = int(input("Enter a number : "))
# if(number>0):
#     print("Positive Number")
# elif(number<0):
#     print("Negative Number")
# else:
#     print("Zero")


# # 4. Largest of Three Numbers
# num1 = int(input("Enter number one : "))
# num2 = int(input("Enter number two : "))
# num3 = int(input("Enter number three : "))

# if(num1>num2 and num1>num2):
#     print(f"Largest Number {num1}")
# elif(num2>num1 and num2>num3):
#     print(f"Largest Number {num2}")
# else:
#     print(f"Largest Number {num3}")


# # 5. Multiplication Table
# num = int(input("Enter the number : "))
# multiplicationTable = 1
# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")


# # 6. Sum from 1 to N
# n = int(input("Enter a number : "))
# sum = 0
# for i in range(0,n+1):
#     sum += i
# print(f"Sum of the n natural number are {sum}")


# # 7. Count Vowels
# name = str(input("Enter your name : "))
# vowels = "aeiouAEIOU"
# count = 0
# for i in name:
#     if i in vowels:
#         count+=1
# print(count)


# # 8. Reverse a String
# name = "Hello World"
# print(name[::-1])


# # 9. Find Maximum in a List
# number  =[1,2,5,6,4,8,3]
# maximum = max(number)
# print(maximum)


# # 10. Count Even Numbers
# list = [1,2,3,4,5,6,7,8,9,10]
# count = 0
# for i in list:
#     if(i%2==0):
#         count+=1
# print(count)


# # 11. Create a Greeting Function
# def greet():
#     name = str(input("Enter name : "))
#     print("Hello! ",name)
# greet()


# # 12. Calculator Function
# def calculator(a,b):
#     operator = input("Enter your operator : ")
#     if(operator == "+"):
#         print(a+b)
#     elif(operator == "-"):
#         print(a-b)
#     elif(operator == "*"):
#         print(a*b)
#     else:
#         print(a/b)
# result = calculator(10,20)

 
# # 13. Student Information
# def student_info(name,age,city):
#     print("Name : ",name)
#     print("Age : ",age)
#     print("City : ",city)
# student_info("Raton Dutta",21,"Kolkata")


# # 14. Lambda Practice
# square = lambda a:a*a
# print(square(5))


# # 15. Student Class
# class student:
#     def __init__(self,name,age,city):
#         self.name = name
#         self.age = age
#         self.city = city
#     def info(self):
#         print("Name : ",self.name)
#         print("Age : ",self.age)
#         print("City : ",self.city)
# s1 = student("Raton Dutta",21,"Kolkata")
# s2 = student("Sayan Pal",25,"Chennai")
# s1.info()
# s2.info()


# # 16. Vehicle → Car
# class vehicle:
#     print("vehicle are fast.")
# class car(vehicle):
#     print("Audi model name")
# print(car)


# # 19. Simple Login System
# name = str(input("Enter your username : "))
# passw = str(input("Enter password : "))

# def loginSystem(username,password):
#     if(username == name and password == passw):
#         print("Login Successful")
#     else:
#         print("Invalid username and password")
# loginSystem("raton","12345")