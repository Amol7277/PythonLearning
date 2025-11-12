
# string1 = str(input("Enter the value ").strip())
string1 = "level"
string2 = ""

for char in reversed(string1):
    string2 += char

print(string2)

if string2 == string1:
    print(string2, "It is Palindrome ")
else:
    print(string2, "It is not Palindrome")
