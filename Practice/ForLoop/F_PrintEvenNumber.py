#Print even numbers between 1 and 20


should_repeat = True
while should_repeat:
    # Code that might lead to the 'if' condition being true
    EvenNumber = int(input("Enter the Number: "))

    if EvenNumber <= 0:
        print("Enter the valid number")
    else:
        for i in range(1, EvenNumber, 1):
            if i % 2 == 0:
                 print(i)

