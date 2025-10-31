#User define functions with Multiple parameter with Return Type

def math_fun(a, b):
    return a+b, a-b, a*b, a/b, a%b

#Multi Variables
sum, sub, mul, div, mod = math_fun(10, 5)

print(sum, sub, mul, div, mod, sep="\n")

print("Addition =",sum)
print("Subtraction =",sub)
print("Multiplication =",mul)
print("Division =",div)
print("modulus =",mod)


# Sub = math_fun(100, 50)
# print(Sub, "\n")
#
# Mul = math_fun(10,10)
# print(Mul, "\n")
#
# Div = math_fun(100, 10)
# print(Div, "\n")
#
# Mod = math_fun(99, 9)
# print(Mod, "\n")
