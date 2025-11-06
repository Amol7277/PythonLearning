#List is a Mutable collection

my_list = [10, 20, 30, 30, "apple", "mango", "apple", 5.5, True, False]
print(my_list)

for i in my_list:
    print(i, end=" | ")

print("\n")

# Copy
print("Copy")
my_list.copy()
print(my_list)

# Append
print("Append")
my_list.append("Banana")
print(my_list)

# Insert
print("Insert")
my_list.insert(1, 15)
print(my_list)

# Remove
print("Remove")
my_list.remove(False)
print(my_list)

# Extend
print("Extend")
my_list.extend([1, 2, 5])
print(my_list)

# POP
print("POP")
my_list.pop()
print(my_list)

# Reverse
print("Reverse")
my_list.reverse()
print(my_list)

print("")
my_list.reverse(), -1
print(my_list)

# Replace
print("Replace")
my_list[1] = 10
print(my_list)

my_list[-1] = 8
print(my_list)

# Counter
print("Counter")
print(my_list.count(30))

# Index value of Item
print("Index")
print(my_list.index(5.5))

# Length
print("Length")
print(len(my_list))

# Sorting & Reverse Sorted
print("Sorting")
my_list2 = [100, 20, 30, 40, 50, 15, 20, 25, 10]
my_list2.sort()
print(my_list2)

print("Sorting Reverse")
my_list2.sort(reverse=True)
print(my_list2)
