# import json

# user = {
#     "name": "Raton",
#     "age": 22,
#     "skills": ["Python", "JavaScript"]
# }

# json_data = json.dumps(user)

# print(json_data)
# print(type(json_data))

import json

json_data = '{"name": "Raton", "age": 22}'

user = json.loads(json_data)

print(user)
print(user["name"])
print(type(user))