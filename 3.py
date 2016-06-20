import math

n=600851475143
primes = []
factors = []

for i in range (2,math.floor(math.sqrt(n))+1):
    for p in primes:
        if i%p==0:
            break
    else:
        primes.append(i)
        if n%i==0:
            factors.append(i)

print (factors[-1])
    
