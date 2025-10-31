# Create a function which will take the 3 values from the user, which are length of the triangle.
# side1, side2, side2
# i/p - int side1 == side2 =side3 → isoceles
# o/p = result in string - iso, eq, scalene


def triangle(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b != c or a == c != b or a != b == c:
        return "Isosceles"
    else:
        return "Scalene"


side1 = int(input("Enter the number 1 : "))
side2 = int(input("Enter the number 2 : "))
side3 = int(input("Enter the number 3 : "))

print("Triangle type is", triangle(side1, side2, side3))

# print(triangle(int(input("Enter the number 1 : ")),int(input("Enter the number 2 : ")), int(input("Enter the number 3 : "))))
