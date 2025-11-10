# Symmetric Difference => It will remove common value from the both set and give the remaining values

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

sym_diff1 = a.symmetric_difference(b)
print(sym_diff1)

sym_diff2 = b ^ a
print(sym_diff2)    # shortcut icon for the Symmatric Difference