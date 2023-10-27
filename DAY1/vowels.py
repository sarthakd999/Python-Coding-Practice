ch = input("Enter a character")

match ch :
    case 'a': print("a is a vowel")
    case 'e': print("e is a vowel")
    case 'i': print("i is a vowel")
    case 'u': print("u is a vowel")
    case 'o': print("o is a vowel")
    case _ :  print(ch," is not a vowel")