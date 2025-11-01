#N number of Argument

def Nargument(*num):
    return num

print(Nargument("Amol","Sonar",14,5,97, True))


def find_min_max(*nums):
    print("Manimum Number is " , max(nums))
    print("Minimum Number is " , min(nums))

find_min_max(10,20,30,5,50,100)