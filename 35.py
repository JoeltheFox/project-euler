import math

def generate_primes(n):                            # generates all primes below n
    sieve = [True] * (math.floor(n/2)-1)
    limit = math.floor((math.floor(math.sqrt(n))-3)/2)     # last number to check
    for i in range(limit+1):
        if (sieve[i]==True):
            for j in range (2*i**2+6*i+3,len(sieve),2*i+3):
                sieve[j]=False
    primes=[2]
    primes.extend([2*k+3 for k in range(len(sieve)) if sieve[k]==True])
    return primes
    
primes = set(generate_primes(1000000))
answers = set()
for p in primes:
    for i in range(1,len(str(p))):
        if int(str(p)[i:]+str(p)[:i]) not in primes:
            break
    else:
        answers.add(p)
print(len(answers))