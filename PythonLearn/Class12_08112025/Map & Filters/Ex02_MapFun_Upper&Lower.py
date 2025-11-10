lowercase = {"honda","hero","yamaha","suzuki","bajaj"}
def upper_case(string1):
    return string1.upper()

up = list(map(upper_case, lowercase))
print(up)


uppercase = ["APPLE","BANANA","MANGO","BLUEBARRY","CRENBARRY"]
def lower_case(string2):
    return string2.lower()

lw = set(map(lower_case, uppercase))
print(lw)