print("Enter the which Test you want to run")
Test_type = str(input("Enter the test type: "))

match Test_type:
    case "API":
        print("Postman API")
    case "Performance":
        print("Jmeter")
    case "UI":
        print("Selenium")
    case _:
        print("Invalid Test")