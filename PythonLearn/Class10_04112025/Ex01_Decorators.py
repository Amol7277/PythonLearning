# Syntax for Decorators

def test1(func):
    def wrapper():
        print("Tejal")
        func()
        print("Sonar")
    return wrapper()

@test1
def test():
    print("Amol")

print("\n")

@test1
def testtest():
    print("Rock")