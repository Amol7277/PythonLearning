try:
    a = int(input("Enter Num1: "))
    b = int(input("Enter Num2: "))
    c = a/b


except ZeroDivisionError:
    print("Division Not possible by Zero")
except ValueError:
    print("String Value not allow")
else:
    print(c)
finally:
    print("I will always be execute")

