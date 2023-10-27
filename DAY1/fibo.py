def fibonacci(limit):
    print(0)
    print(1)
    a = 0
    b = 1
    while(limit != 0):
        
        sum = a + b
        print(sum,end=" ")
        a = b
        b = sum
        limit -= 1

l = int(input("Enter limit = "))
fibonacci(l)