keys = ["name", "role", "experience", "abc"]
values = ["Aman", "SDET", 3]

dict1 = dict(zip(keys,values))
print(dict1)


my_dict1 = dict(Name="Amol",Role="QA",Age=28,Experience = 4.6)
my_dict2 = dict(Name1="Aman",Role1="SDET",Age1=30,Experience1 = 5.1)

# my_dict1 = {"Name" : "Amol", "Role" : "QA"}
# my_dict2 = {"Name1" : "Aman", "Role1" : "SDET"}


dict2 = my_dict1 | my_dict2
print(dict2)
print(dict2.get("Name1"))




