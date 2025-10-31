#divisible by 3 then print Fizz
#divisible by 5 then print Buzz
#divisible by both 3 & 5 then print FizzBuzz

# numbers = int(input("enter number: "))

# for i in range(1, numbers):
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
