# ✅ Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

mark = int(input("Enter the Mark: ").strip())

if mark<0 or mark>100:
    print("Mark is out of range")
else:
    if mark>=90 and mark<=100:
        print("A Grade student")
    elif mark>=80 and mark<=89:
        print("B Grade student")
    elif mark>=70 and mark<=79:
        print("C Grade student")
    elif mark>=60 and mark<=69:
        print("D Grade student")
    else:
        print("F Grade student and You are fail")