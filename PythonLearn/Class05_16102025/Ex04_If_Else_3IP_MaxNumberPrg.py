# Checked the Max number

num1 = float(input("Enter a number 1: "))
num2 = float(input("Enter a number 2: "))
num3 = float(input("Enter a number 3: "))

if num1 >= num2 and num1 >= num3:
    print("Max number is ", num1)
elif num2 >= num3 and num2 >= num1:
    print("Max number is ", num2)
else:
    print("Max number is ", num3)