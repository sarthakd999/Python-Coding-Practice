# 1) create 3 functions "show1()","show2()" and "show3()"
# now define a function "caller" in such a way that it can accept any function as an argument and invoke the same.

# invoke caller function by passing show1,show2 and show3


def show1():
    print("I am show1")

def show2():
    print("I am show2")    

def show3():
    print("I am show3")

def caller(fun):
    if(callable(fun)):
        fun()
    else:
        print("You have not passed a function name")   

caller(show1)
caller(show2)
caller(show3)
# caller(apple)
caller(1)
