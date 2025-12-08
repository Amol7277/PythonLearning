try:
    a = int(input("Enter Num1: "))
    b = int(input("Enter Num2: "))
    c = a/b
    print(c)

except (ValueError, ZeroDivisionError, TypeError, IndexError, NameError):
    print("Error because of Value, Type, ZeroDiv,Index, or Name")
