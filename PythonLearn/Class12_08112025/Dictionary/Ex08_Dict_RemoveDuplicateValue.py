#  Remove duplicate values from a dictionary.

my_dict = {"a": 1, "b": 2, "c": 1, "d": 3}
# test = set(my_dict.values())
# print(test)


unique_value=set()
result = {}

for key, value in my_dict.items():
    if value not in unique_value:
        result[key]= value
        unique_value.add(value)

print(result)
print(unique_value)
