### LIST ###
# Create
#    ↓
# Index
#    ↓
# Slice
#    ↓
# append()
#    ↓
# remove()
#    ↓
# pop()
#    ↓
# sort()

# numbers = [10, 20, 30, 40, 50, 60]
# print(numbers[2])
# print(numbers[5])
# print(numbers[1:4])
# print(numbers[3:])
# print(numbers[-1])


# # append() is used to add a new item to the end of a list.
# numbers = [10,20,30,40]
# numbers.append(50)
# numbers.append(60)
# print(numbers)


# remove() removes an item based on its value.
# numbers = [10,20,30,40,50,60]
# numbers.remove(30)
# numbers.remove(50)
# print(numbers)


# # pop() removes the item at INDEX
# numbers = [10,20,30,40,50,60]
# numbers.pop(2)
# numbers.pop()
# print(numbers)


# # sort() arranges the list in ascending order.
# numbers = [20,50,40,10,30,80,60,70]
# numbers.sort()
# print(numbers)


# numbers = [50, 20, 80, 30, 10, 60, 40, 70]
# numbers.append(90)
# numbers.remove(30)
# numbers.pop(2)
# numbers.sort()
# print(numbers)
# print(numbers[:3])


### TUPLES ###
# A tuple is a collection of values, just like a list, but a tuple is immutable.
# student = ("Raton",21,"CSE","Kolkata")
# print(student[0])
# print(student[1])
# print(student[-1])
# print(student[:3])

# student[1] = 22  # checking the tuple immutability
# print(student)

# numbers = (10, 20, 30, 20, 40, 50, 20, 60)
# print(numbers.count(20))
# print(numbers.index(20))
# print(numbers.count(10))
# print(numbers.index(50))


### SET ###
# A set is a collection that stores unique values.
# A = {10, 20, 30, 40, 50}
# B = {40, 50, 60, 70, 80}

# print(A.union(B))  # Union
# print(A.intersection(B))  # Intersection
# print(A.difference(B))  # Difference
# print(A.symmetric_difference(B))  # Symmetric Difference


# # Membership Test
# numbers = {10, 20, 30, 40, 50}
# print(30 in numbers)
# print(100 in numbers)
# print(100 not in numbers)


### DICTIONARY ###
# A dictionary stores data as key-value pairs.

# get()     → get a specific value
# keys()    → get all keys
# values()  → get all values
# items()   → get keys + values

student = {
    "name": "Raton",
    "age" : 21,
    "course" : "CSE",
    "city" : "Kolkata"
}

# print(student["name"])
# print(student.get("age"))
# for key in student.keys():
#     print(key)
# for value in student.values():
#     print(value)
# for key,value in student.items():
#     print(key," : ",value)

# student["age"] = 22  # Update the value of a key
# print(student["age"])
# student["email"] = "raton22@gmail.com"
# print(student["email"])  # Add a new key-value pair
# print(student)
# for key,value in student.items():
#     print(key," : ",value)


## Exercises
# 1. Store five favourite movies in a list and print each one
# movies = ["Inception", "The Dark Knight", "Interstellar", "The Matrix", "Pulp Fiction"]
# for movie in movies:
#     print(movie)


# 2. Remove duplicates from a list using a set.
# numbers = [10,20,10,30,10,40,20,50]
# set_value = sorted(set(numbers))
# for i in set_value:
#     print(i)


# 3. Create a student dictionary with name, age and marks.
# student = {
#     "name" : "Raton Dutta",
#     "age" : 21,
#     "marks" : 69
# }

# print(student)

# for key,value in student.items():
#     print(key," : ",value)