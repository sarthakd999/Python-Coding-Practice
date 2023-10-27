# define a function in such a way that it can accept n number of values and print their sum. [ variable number of arguments]

def add(*num):
    sum = 0
    for i in num:
        sum += i

    print("sum is = ",sum)

add(1,2,3,4,5)