# print("hello world")
# for i in range(1,3):
#     print(i)


# i = 1
# while(i<10):
#     print(i)
#     i = i+1

# ch = input()
# print(ch)    

# print(i)   

# a=100
# print(a)
# print("The number is",a)
# print("The datatype of a is",type(a))

# a=4.5
# print(a)
# print("The number is",a)
# print("The datatype of a is",type(a))

# c = "Hello"
# print("The datatype of a is",type(c))

# d = False
# print("The datatype of a is",type(d))

# e = 'a'
# print("The datatype of a is",type(e))

# x = 'a'
# y = int(x)
# print(y)


# a=65
# b=20
# print("Addition is", a+b)
# print("Subtraction is", a-b)
# print("Multiplication is", a*b)
# print("Division is", a/b)
# print("Remainder is", a%b)
# print("Floor Division is", a//b)

# # g = 10
# # b = 10
# a=3
# match a:
#         case 5:
#                 print("it is 5")
#         case 7:
#                 print("it is 7")
#         case _:
#                 print("not a desired number")


# a=input("enter course : ")
# match a:
#         case 5:
#                 print("it is 5")
#         case 7:
#                 print("it is 7")
#         case _:
#                 print("not a desired number")

# for i in range(0,5):
#     if i==2:
#         break
#     print(i)
# else:
#     print("done")


# x=3
# x+=2
# x-=3
# x*=5
# x/=2
# x%=3
# print(x)

# n=int(input("Enter a number"))
# i=1
# while i<=n:
#     print(i,end=' ')
#     i+=1

# print("Done")

expense_list=[1230,2240,1500,1678,2020,1580,2240,1450,'1500',1245,2300]
total_expense=0

for expense in expense_list:
    total_expense+=expense

print("total expense is \t",total_expense)



