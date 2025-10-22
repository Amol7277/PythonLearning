# Print even numbers between 1 and 20


should_repeat = True

while should_repeat:
# Code that might lead to the 'if' condition being true
    EvenNumber = int(input("Enter EvenNumber: "))

    i = 1
    while i <= EvenNumber:
        if i % 2 == 0:
            print(i)
        i += 1
