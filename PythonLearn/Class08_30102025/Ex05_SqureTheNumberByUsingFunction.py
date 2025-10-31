# Create a function which will take a positive number from the user and perform square of the number?

def number(a):
    if a < 0:
        print("Enter Valid Number")
    else:
        print("Square of the Number is =", a*a)

number(int(input("Enter the validation = ")))
