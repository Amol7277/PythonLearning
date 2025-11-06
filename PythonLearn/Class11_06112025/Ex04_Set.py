# Set is an unordered collection of data types that is iterable, immutable and has **no duplicate elements.**

my_set = {1,2,10,15,3,3, 7, 8, 9}
print(my_set)

for i in my_set:
    print(i)

my_set.remove(10)
print(my_set)

my_set.pop()
print(my_set)