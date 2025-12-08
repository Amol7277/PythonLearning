eg = ExceptionGroup("Multiple Ex", [TypeError("Type Error"), ValueError("Value Error"), ZeroDivisionError("Zero divisible Error")])

def check_div(a):
    if a == 0:
        raise eg

check_div(1)