marks = int(input("Enter marks = "))

if (marks > 90):
    print("Distinction")
elif (marks < 90 and marks >= 75 ) :
    print("First Class")    
elif(marks < 75 and marks >= 60):
    print("Second class")
elif(marks < 60 and marks >= 50 ):
    print("pass")    
else:
    print("fail")


    

