# Checking for a Leap Year , 2024 => Yes
# Leap day occurs in each year that is a multiple of 4,
# Except for years evenly divisible by 100 but not by 400.

for i in range(2000, 2030):
    if i % 4 ==0 or i % 100 == 0 and i % 400 != 0:
        print(i)




