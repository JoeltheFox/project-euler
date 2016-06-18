import math
import numpy as np

primes = []
for i in range(2,math.floor(math.sqrt(987654321))+1):
    for prime in primes:
        if i % prime == 0:
            break
    else:
        primes.append(i)

def is_prime(x):
    sqrt_x = math.sqrt(x)
    for prime in primes:
        if prime > sqrt_x:
            return True
        if x % prime == 0:
            return False
    return True

primes = np.array(primes)
def is_prime_fast(x):
    return not np.any(np.mod(x, primes) == 0)

def num_digits(x):
    return math.floor(math.log10(x))+1

def is_pandigital(x):
    chars = set(map(int,list(str(x))))
    return chars == set(range(1,num_digits(x)+1)) and len(chars) == num_digits(x)

def digits2int(digits):
    return int(''.join(map(str,digits)))

def next_pandigital(x):
    n=num_digits(x)
    
    if x == digits2int(list(range(1,n+1))):
        return digits2int(list(range(n-1,0,-1)))

    digits = list(map(int,list(str(x))))

    for i in range(n-2,-1,-1):
        sorted_d=sorted(digits[i:])
        if digits[i:]==sorted_d:
            continue
        # find the largest number in digits[-i+1:] that is < digits[-i]
        largest_i = i+1
        for k in range(i+1,n):
            if digits[k]<digits[i] and digits[k]>=digits[largest_i]:
                largest_i=k
        # print("%d %d" % (i, largest_i))
        digits[i], digits[largest_i] = digits[largest_i], digits[i]
        digits[i+1:]=sorted(digits[i+1:], reverse=True)
        return digits2int(digits)
  
# best=7652413
# print(is_prime(best))
# print(is_pandigital(best))
x = 987654321
while x > 1:
    if is_prime(x):
        print("The largest prime pandigital number is", x)
        break
    x = next_pandigital(x)
    # print(x)
