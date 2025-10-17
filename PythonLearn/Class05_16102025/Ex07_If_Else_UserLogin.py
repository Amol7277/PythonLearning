#Check if the user can log in based on correct username and password.

# I/p
#
# username = "admin"
# password = "1234"

username = str(input("Enter username: ").strip())
password = int(input("Enter password: ").strip())

if username == "admin" and password == 1234:
    print("Login Successful")
else:
    print("Invalid credentials")