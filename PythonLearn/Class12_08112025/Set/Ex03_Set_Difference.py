# Set Difference => It will give the uniques value which is not present in other set.

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

diff1 = a.difference(b)
print("Difference ", diff1)

diff2 = b.difference(a)
print("Difference ", diff2)

diff3 = a - b               # shortcut icon for the Difference
print("Difference ", diff3)

diff4 = b - a               # shortcut icon for the Difference
print("Difference ", diff4)