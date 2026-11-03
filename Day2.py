# # Check a number weather its positive or negative
# n = int(input("Enter a number : "))
# if(n > 0):
#     print("Positive Number.")
# elif(n<0):
#     print("Negative Number")
# else:
#     print("Zero")


# # Print number 1 to 20
# for i in range(1,21):
#     print(i)


# # Print the multiplication table
# n = 5
# i = 1
# while(i<=10):
#     print(f"{n} X {i} = {n*i}")
#     i+=1


# # Find the sum of the number of 1 to n
# n = int(input("Enter the value of n : "))
# sum = 0
# for i in range(1,n+1):
#     sum += i
#     i+=1

# print(sum)


# #Number Guessing Game
# import random

# number = random.randint(1, 100)

# while True:
#     n = int(input("Guess a number between 1 to 100: "))

#     if n == number:
#         print("You guessed it right! 🎉")
#         break
#     elif n < number:
#         print("You guessed low. Pick a higher number.")
#     else:
#         print("You guessed high. Pick a lower number.")