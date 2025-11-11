# Frequency of Characters in a String
# Write a program to count the frequency
# of each character in a given string.

mystr = "Python_Packages"
mydict = {}

for char in mystr:
    mydict[char] = mydict.get(char, 0) + 1

print(mydict)