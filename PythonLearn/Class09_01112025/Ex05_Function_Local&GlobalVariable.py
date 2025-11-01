#Local & Global variable in side the Functions

global_var = "Amol"

def outer_fun():
    print(global_var)

    def inner_fun1():
        local_var = "Sonar"
        print(local_var)

    def inner_fun2():
        local_var = "Tejal"
        print(local_var)

        def inner_fun3():
            local_var = "Patel"
            print(local_var)

        inner_fun3()

    inner_fun1()
    inner_fun2()


outer_fun()