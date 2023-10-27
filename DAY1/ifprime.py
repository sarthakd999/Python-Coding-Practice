def check_prime(num):
    for i in range(2,num):
        if(num % i == 0):
            print(num,"It is not a prime")    
            break
        else:
            print(num,"It is prime")    
            break

check_prime(20)  
check_prime(10)  
check_prime(13)  
check_prime(11)  
check_prime(15)  
check_prime(17)  




