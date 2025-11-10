dict = {
    "Name" : "Amol Sonar" ,
    "Address" : "Dindoli" ,
    "Age" : 28 ,
    "Height" :  5.9 ,
    "Male" : True
}

print(dict)

print(dict["Name"])
print(dict["Address"])
print(dict["Age"])
print(dict["Height"])
print(dict["Male"])

print("\n")
for key,value in dict.items():
    print(key,":",value)
    print(key)
    print(value)

dict["Name"] = "Sonar Amol"
print(dict)

dict["Address"] = "96/97 Dindoli"
print(dict)
