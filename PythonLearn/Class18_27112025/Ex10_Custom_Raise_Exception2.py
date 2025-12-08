

def drink(age):
    if 0 < age < 18 :
        raise Exception("Not correct age of drink")     #Custom Exception
    elif age < 0:
        raise ValueError("Enter Valid age")         # Built in Exception
    else:
        return "You can drink Tea"

print(drink(22))
print(drink(15))
print(drink(-1))

