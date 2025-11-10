# Set Union => It will give the all value from the both the set but not repeat the common value.

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

union1 = a.union(b)
print(union1)

union2 = b | a          # shortcut icon for the Uniorn
print(union2)