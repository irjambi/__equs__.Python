import time 
t0 = time.time() 

a = input()
a = [int(a)]
for k in a: 
    if k > 1: 
        for i in range(2,k): 
            if k%i == 0: 
                print("{prime} is a not prime number".format(prime=k)) 
                break 
        else:  
            print("{prime} is a prime number".format(prime=k))#, ' is a prime number') 
    else: 
        #print(k,' is not a prime number') 
        break  
    k = k+1 
t1 = time.time() - t0 
#print(t1)    