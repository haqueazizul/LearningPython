user = {
    "Name": "Azizul Haque",
    "Age": 28,
    "Email": "sparkeraziz4@gmail.com",
    "is_Verified": True
}


user["Age"] = 29
user["Job"] = "Teaching"
print(user.get("Age"))
print(user)
print(user.get("password"))
print(user.get("Job"))