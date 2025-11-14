class Math:
    a = None
    b = None
    c = None

    def __init__(self):
        print("Calculate by All Operators")

    def sum(self,a,b,c):
        return print("Summation is ", a+b+c)

    def sub(self,a,b,c):
        return print("Subtraction is", a - b - c)

    def mul(self,a,b,c):
        return print("Multiplication is", a*b*c)

    def div(self,a,b):
        return print("Division is", a/b)

cal_c = Math()
cal_c.sum(30,20,10)
cal_c.sub(30,20,10)
cal_c.mul(30,20,10)
cal_c.div(30,20)







