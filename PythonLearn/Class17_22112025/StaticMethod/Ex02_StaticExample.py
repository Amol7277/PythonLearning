class Timecount:
    count = 0
    def __init__(self):
        Timecount.count += 1

t1 = Timecount()
t2 = Timecount()
t3 = Timecount()
t4 = Timecount()

print(Timecount.count)

