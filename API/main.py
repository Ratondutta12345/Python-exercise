# import requests
# response = requests.get("https://api.github.com/users/Ratondutta12345")
# data = response.json()
# print(data)
# print("Username:", data["login"])
# print("Followers:", data["followers"])
# print("Public Repositories:", data["public_repos"])
# print("Profile Url:", data["html_url"])


# response = requests.get("https://api.github.com/users/Ratondutta12345")
# try:
#     response.raise_for_status()
#     data = response.json()
#     print("Username:", data["login"])

# except requests.exceptions.HTTPError as error:
#     print("API Error:", error)


## Post request
# import requests

# url = "https://httpbin.org/headers"

# token = "my_secret_token"

# headers = {
#     "Authorization": "Bearer YOUR_TOKEN"
# }

# response = requests.get(url, headers=headers)

# print(response.json())


# import requests

# url = "https://httpbin.org/post"

# data = {
#     "name": "Raton",
#     "course": "Python"
# }

# response = requests.post(url, json=data)

# print(response.status_code)
# print(response.json())


# import requests

# url = "https://httpbin.org/post"

# headers = {
#     "Content-Type": "application/json",
#     "Authorization": "Bearer YOUR_TOKEN"
# }

# data = {
#     "name": "Raton",
#     "course": "Python"
# }

# response = requests.post(
#     url,
#     json=data,
#     headers=headers
# )

# print(response.status_code)
# print(response.json())


# import requests

# url = "https://httpbin.org/put"

# data = {
#     "name" : "Raton",
#     "id": 101
# }

# response = requests.put(url,json=data)

# print(response.status_code)
# print(response.json)


# import requests

# url = "https://httpbin.org/patch"

# data = {
#     "name" : "Raton"
# }

# response = requests.patch(url, json=data)

# print(response.status_code)
# print(response.json)


# import requests

# url = "https://httpbin.org/delete"

# response = requests.delete(url)

# print(response.status_code)
# print(response.json())


# import requests

# url = "https://api.github.com/user"

# headers = {
#     "Authorization": "Bearer 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"
# }

# response = requests.get(url, headers=headers)

# print(response.status_code)
# print(response.json())


# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()

# token = os.getenv("GITHUB_TOKEN")

# url = "https://api.github.com/user"

# headers = {
#     "Authorization": f"Bearer {token}"
# }

# response = requests.get(url, headers=headers)

# print(response.status_code)
# print(response.json())