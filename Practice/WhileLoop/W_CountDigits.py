# Count digits in a number

Num = int(input("Enter the Number: "))
# digit = len(Num)
# print(digit)

digit = 0

while Num > 0 :
    digit += 1
    Num = Num // 10
print(digit)

