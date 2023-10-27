# 2) define nested function and show how will you invoke it.


def mobile():
    def simcard():
        print("hey I am simcard I am inside your phone.")
    print("I am your mobile phone")    
    return simcard

var = mobile()
var()