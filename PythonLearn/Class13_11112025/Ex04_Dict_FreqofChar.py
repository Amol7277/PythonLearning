# Frequency of Characters in a String
# Write a program to count the frequency
# of each character in a given string.

# string = "Automation"
string = str(input("Enter the Name: "))
char_count = {}

for char in string:
    char_count[char]=char_count.get(char,0)+1
print(char_count)
