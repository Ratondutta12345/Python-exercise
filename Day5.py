### STRING ###
# String indexing
# name = "Raton Dutta"
# print(name[0])
# print(name[-1])
# print(name[:6])
# print(name[6:])
# print(name[::-1])
# print(name[6])


# String methods
# lower()
# upper()
# strip()
# replace()
# split()
# join()
# text = "   Hello Raton, Welcome to Python   "
# print(text.lower())
# print(text.upper())
# print(text.strip())
# print(text.replace("Raton","Developer"))
# print(text.split())

# languages = ["Python", "JavaScript", "React"]
# print(", ".join(languages))


# Error Handling
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     print(num1/num2)
# except ValueError:
#     print("Enter a valid number")
# except ZeroDivisionError:
#     print("0 cannot eb divided by anu number.")
# finally:
#     print("Calculation finished.")


# Exercise
# 1. Count the number of vowels in a sentence.
# name = str(input("Enter a sentence: "))
# vowel = "aeiouAEIOU"
# count = 0
# for i in name:
#     if i in vowel:
#         count+=1
# print(f"Number of vowels in the sentence is : {count}")


# 2. Ask for a full name and print it in title case.
# name = str(input("Enter your name : "))
# print(name.title())


# 3. Use random to generate a random number.
# import random
# number = random.randint(1,100)
# print(number)


# 4. Handle invalid number input with try/except.
# try:
#     num = int(input("Enter a number: "))
#     print(f"You entered: {num}")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# finally:
#     print("Input handling finished.")