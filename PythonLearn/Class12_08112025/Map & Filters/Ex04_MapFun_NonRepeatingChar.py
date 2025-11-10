# Find the first non-repeating character in a string using sets.
# swiss -> s -x , w - Answer

# print("swiss".count("s"))
# print("swiss".count("w"))
# print("swiss".count("i"))


def nonRepeat(string):
    for i in string:
        if string.count(i) == 1:
            return i
    return None

character = nonRepeat("swiss")
print(character)


d = set()
def nonRepeat(string):
    for i in string:
        if string.count(i) == 1:
            d.add(i)
            return i
    return None

character1 = nonRepeat("Reddy")
character2 = nonRepeat("pythonProject")
print(character1)
print(character2)
print(d)