A_Integer = 101
A_String = "Amol"
A_Float = 5.55
A_Boolean = True
A_Complex = 5 + 5j

print(type(A_Integer),end="\n\n")  #<class 'int'>

print(type(A_String),end="\n\n")  #<class 'str'>

print(type(A_Float),end="\n\n")  #<class 'float'>

print(type(A_Boolean),end="\n\n")  #<class 'bool'>

print(type(A_Complex),end="\n\n")  #<class 'complex'>

print(type(A_Complex.real),end="\n\n")  #<class 'float'>

print(type(A_Complex.imag),end="\n\n")  #<class 'float'>

print((type(A_Integer), type(A_String), type(A_Float), type(A_Boolean), type(A_Complex), type(A_Complex.real)))