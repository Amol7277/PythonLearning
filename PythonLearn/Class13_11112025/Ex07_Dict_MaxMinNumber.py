mydict1 = {"A": 10, "B": 50, "C": 100}


def maxvalue():
    return max(mydict1.values())


print("Maximum Value", maxvalue())


def maxkey(mydict1):
    return max(mydict1.keys())


print("Maximum Key", maxkey({"A": 10, "B": 50, "C": 100}))


def minvalue():
    return min(mydict1.values())


print("Minimum Value", minvalue())


def minkey(mydict1):
    return min(mydict1.keys())


print("Minimum Key", minkey({"A": 10, "B": 50, "C": 100}))
