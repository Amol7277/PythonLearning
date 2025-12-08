def testing(id):
    if id != "Admin":
        raise Exception ("Invalid ID")
    return "Welcome Admin"

# print(testing("Amol"))
print(testing("Admin"))


