def add():
    print("add")

def modify():
    print("modify")

def delete():
    print("delete")    

def accept():
    num = int(input("Enter a number from 1 to 3"))

    match num:
        case 1: add()
        case 2: modify()
        case 3: delete()    

accept()        