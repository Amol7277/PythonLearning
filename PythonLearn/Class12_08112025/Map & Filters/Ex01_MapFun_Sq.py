my_list = [1, 2, 3, 4]

def square(a):
    return a ** 2

square_number = list(map(square, my_list))
print(square_number)
