# Set Intersection => It will give the common value from two sets

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

i_section1 = a.intersection(b)
print(i_section1)

i_section2 = b & a      # shortcut icon for the intersection
print(i_section2)