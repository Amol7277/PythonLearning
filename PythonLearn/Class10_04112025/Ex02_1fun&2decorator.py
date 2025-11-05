# 1 main function & 2 decorators

def honda(func):
    def wrapper():
        print("I like Royal Enfield bullet")
        func()
        print("But I want Himalayan Bike")
    return wrapper

def hero(func):
    def wrapper1():
        print("Hero splender")
        func()
        print("Hero honda")
    return wrapper1

@hero
@honda
def bike():
    print("But I also like Honda Unicorn")
bike()