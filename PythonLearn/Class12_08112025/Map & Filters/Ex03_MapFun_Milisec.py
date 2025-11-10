mili = [1000, 1500, 2000, 3000, 5000]

def milisecond(sec):
    return sec * 1000

mili1 = list(map(milisecond, mili))
print("Miliseconds ", mili1)


second = [1000, 1500, 2000, 3000, 5000]

def seconds(sec):
    return sec / 1000

second1 = list(map(seconds, second))
print("Seconds ", second1)