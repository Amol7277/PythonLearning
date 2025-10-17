# Write the program if the Age if greater than 21 then he can go to club.

age = int(input("The age of the person: ").strip())

if age <= 0 or age > 100:
    print("Enter the valid age")
else:
    if age >= 21:
        print("You can go to the club")
    else:
        print("you can't go to the club")
