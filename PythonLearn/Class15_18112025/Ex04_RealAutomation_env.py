from dotenv import load_dotenv
import os

# load_dotenv()
#
# print("Username from env:", os.getenv("USERNAME1"))
# print("Password from env:", os.getenv("PASSWORD"))
# print("Password from env:", os.getenv("PASSWORD2"))

class LoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        load_dotenv()
        if self.email == os.getenv("USERNAME1") and self.password == os.getenv("PASSWORD"):
            print("Login Successfully")
        else:
            print("Invalid Credential")



email = input("Enter the email ID: ").strip()
password = input("Enter the Password: ").strip()

login = LoginPage(email, password)
login.login_confirm()

print(os.getenv("USERNAME1"), os.getenv("PASSWORD"))