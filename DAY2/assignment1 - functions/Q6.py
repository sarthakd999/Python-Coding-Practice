def change(ch):
    d = ord(ch)
    if d >= 65 and d <= 90:
        d = d + 32
        print(chr(d))
    else: 
        d = d - 32
        print(chr(d))  

change('a')         
change('Z')

