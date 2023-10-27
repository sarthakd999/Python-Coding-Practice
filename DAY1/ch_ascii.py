s = input("Enter a character : ")

asci = ord(s)
print(asci)

if(asci >= 97 and asci <= 122):
    print("Lower case")
elif(asci >= 65 and asci <= 90):
    print("Upper case")
else:
    print("invalid char")       