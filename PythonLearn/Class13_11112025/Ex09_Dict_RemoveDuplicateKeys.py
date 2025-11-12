#  Remove duplicate Keys from a dictionary.

my_dict = {"a": 1, "b": 2, "a": 1, "d": 3}

uniqueKey = set()
result = {}

for key,value in my_dict.items():
    if key not in uniqueKey:
        result[key]=value
        # uniqueKey.add(key)

print(result)
