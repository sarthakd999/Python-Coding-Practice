# write a function to accept minimum 3 characters and maximum 5 characters. 
#  	[ use default arguments method ]

def checkLength(*varg):
    if varg.__len__() >= 3 and varg.__len__() <= 5:
        print(varg)
    else:
        print("not of supported length")  

checkLength(1,2,3,4,5)
checkLength(1,2,3,4,5,6,7)           
checkLength(1)