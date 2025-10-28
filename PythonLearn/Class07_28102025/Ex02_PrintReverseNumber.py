Num = int(input("Enter the number: "))

if 0 < Num <= 100:
    for i in range(Num, 0, -1):
        print(i, end = " ")
else:
    print("Please Enter Valid Number")
