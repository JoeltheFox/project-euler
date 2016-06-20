"""this solves ProjectEuler problem 27, which asks what coefficients a,b result in most
primes generated from function n^2 + an + b, starting at n=0. |a| and |b| < 1000

This program generates primes to check against, then loops through all possible a's 
and b's (and signs of a,b) and checks how many primes they generate before failing

A function to extend list of primes is needed because we don't know a priori how large
the primes we need to check will"""

import math

def extend_primes(primes, n):               #generates further primes up to n, given primes already found
    i = primes[-1]+2                       #first candidate is last prime +2
    while i<n:
        for p in primes:     # check for prime factors up to sqrt(candidate), if none then is prime
            if i%p==0:        #not prime 
                break      
            elif p>=math.sqrt(i):        #if past sqrt(candidate) with no prime factors, then is prime
                primes.append(i)
                break
        i+=2                     # next prime candidate is 2 higher, assuming the prime 2 was already found
    return primes
    
    
def func(x,a,b,sign):   # returns x^2 +ax +b, with signs of a,b given by 'sign'
    return (x**2 + a*x*sign[0] + b*sign[1])
        

starting_primes = [2,3]
prime = extend_primes(starting_primes, 10000)   #generates all primes up to 10,000
    
longest = 0          # longest chain of primes
longestabs = (0,0,(1,1))    # values of a,b,sign that generates longest chain

signs = [(1,1),(-1,1),(1,-1),(-1,-1)]      # all possible pairs of signs for a and b



for i in range(1000):    #represents 'a'
    for j in range(1000):     #represents 'b'
        for s in signs:         #signs of 'a' and 'b'
            k=0                #represents 'n'
            while(True):      # loop to terminate once a non-prime is found
                x=func(k,i,j,s)
                if x > prime[-1]:     #if list of primes is too short, ~double it
                    prime = extend_primes(prime, 2*x)
                if x in prime:         #if current result is prime, continue looping and increment
                    k += 1
                elif k-1 > longest:      #once the function runs out of primes, checks if new record was made
                    longest = k-1
                    longestabs = (i,j,s)   #saves values that generated most primes
                    break
                else:                 #function ran out of primes and record was not made.
                    break
                
                
print (longestabs)
