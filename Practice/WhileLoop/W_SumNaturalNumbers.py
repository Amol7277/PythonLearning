# Sum of first N natural numbers

ShouldRepeat = True
while ShouldRepeat:

    num = int(input('Enter a number: '))
    sum = 0
    i = 0
    while i < num:
        sum += i
        i += 1
    print("The sum is: ", sum)