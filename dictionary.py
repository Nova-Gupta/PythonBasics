user = {
    "name": "Nova",
    "age": 20,
    "city": "India"
}
print(user["age"])
user["age"] = 19
print(user["age"])
user["email"] = "nova@gmail.com"
print(user)
print(user.keys())
print(user.values())
print(user.items()) 
for key, value in user.items():
    print(f"{key}: {value}")
del user["city"]
print(user) 
user.pop("email")
print(user)