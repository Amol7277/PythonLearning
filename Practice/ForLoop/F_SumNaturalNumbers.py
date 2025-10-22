# Sum of first N natural numbers

ShouldRepeat = True
while ShouldRepeat:


    Num = int(input("Enter a number: "))
    Sum = 0

    if Num > 0:
        for i in range(1, Num, 1):
            Sum = Sum + i
        print("The sum is: ", Sum)
    else:
        for i in range(-1, Num, -1):
            Sum = Sum + i
        print("The sum is: ", Sum)
