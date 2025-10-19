# Given a Number a number you need to calculate the factorial of that number
# n = 5
# Fact = 5×4×3*2*1 = 120

Number = int(input("Enter a number: ").strip())
fact = 1

# Method 1 #

for i in range(Number, 0, -1):
    fact = fact * i
print("Factorial of the", Number, "=", fact)

# Method 2 #

# for i in range(1, Number, 1):
#     fact = fact * i
# print("Factorial of the", Number-1, "=", fact)

# Method 3 #

# import math
#
# factorial = math.factorial(5)
# print(factorial)

# Method 4 #

# i = Number
# while i > 0:
#     fact = fact * i
#     i = i - 1
# print(fact)



