# find the given positive number is even or odd

num = int(input("Enter a number: ").strip())
if num >=0:
    if num % 2 == 0:
        print("Even number")
    else:
        print("odd number")
else:
    print("It's a negative number")