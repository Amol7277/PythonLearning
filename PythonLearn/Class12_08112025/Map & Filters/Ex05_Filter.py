My_List1 = [10, 21, 14, 25, 30, 40]
My_List2 = ["Amol","", "Tejal","Nirali","","Radhika"]
My_List3 = ["Pass","Fail","Skip","Continue"]

def filtervalue1(string):
    return string % 2 == 0

test1 = list(filter(filtervalue1, My_List1))
print(test1)

r1=list(filter(lambda x: x%2==1, My_List1))
print(r1)

test2 = list(filter(None,My_List2))
print(test2)

def filtervalue1(string):
    return string !="Pass"

test3 = list(filter(filtervalue1,My_List3))
print(test3)


test4 = list(filter(lambda y: y=="Fail", My_List3))
print(test4)


s = set(i**2 for i in range(5))
print(s)
l = list(i**2 for i in range(5))
print(l)