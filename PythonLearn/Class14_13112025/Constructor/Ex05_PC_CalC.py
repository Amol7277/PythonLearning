class Math:
    a = None
    b = None
    c = None

    def __init__(self,a1,b1,c1):
        self.a = a1
        self.b = b1
        self.c = c1
        print("Calculate by All Operators")

    def sum(self):
        return print("Summation is ", self.a + self.b + self.c)

    def sub(self):
        return print("Subtraction is", self.a - self.b - self.c)
    def mul(self):
        return print("Multiplication is", self.a * self.b * self.c)

    def div(self):
        return print("Division is", self.a / self.b)

cal_c = Math(100,50,20)
cal_c.sum()
cal_c.sub()
cal_c.mul()
cal_c.div()