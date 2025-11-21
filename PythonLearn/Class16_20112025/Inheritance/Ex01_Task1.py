class BaseTest:
    _driver = "Chrome"

    def setup(self):
        print("Launching browser: ", self._driver)


    def teardown(self):
        print("Closing browser")


class LoginTest(BaseTest):

    def run_test(self):
        self.setup()

        __username = str(input("Enter User Name: "))
        __password = int(input("Enter Password: "))

        if __username == "admin" and __password == 12345:
            print("Running login test with user: ", __username)
        else:
            print("Invalid Credential")
        self.teardown()


login = LoginTest()
login.run_test()
