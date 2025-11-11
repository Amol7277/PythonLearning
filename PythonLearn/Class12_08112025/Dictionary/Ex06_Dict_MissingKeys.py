mydict1 = { "a": 1, "b": 2, "c" : "c" }
mydict2 = { "a": 1, "b": 2 }
mydict3 = {"e" :4 ,"d": 5 }

missing_key = set(mydict1.keys() - mydict2.keys() - mydict3.keys())
missing_key1 = set(mydict2.keys() - mydict3.keys())
print(missing_key)
print(missing_key1)
