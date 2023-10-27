# define a function which accepts a string , toggle and return it.
# 	[ hint :  use "swapcase()" function of string ]

def casetoggler(str):
    newstr = str.swapcase()
    print(newstr)

sent = input ("Enter a string : ")
casetoggler(sent)