# num1 = int(input("Enter the 1st number: ").strip())
# num2 = int(input("Enter the 2nd number: ").strip())
# num3 = int(input("Enter the 3rd number: ").strip())
num3 = int(input("Enter the 3rd number: ").strip())

def sumof3number(n1=100, n2=200, n3=300):
    return n1+n2+n3

print(sumof3number())

result = sumof3number(n1=10, n2=20, n3=num3)
print(result)
