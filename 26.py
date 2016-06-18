# Solves ProjectEuler problem 26: https://projecteuler.net/problem=26

n=1000
longest=0    #longest cycle
longestd=0    #index of longest cycle

for i in range(2,n):
    x=[(1,0)]           # [(remainder, digit)]
    numerator=1
    cycle=0
    while(cycle==0):   # long division until cycle is found, ie when there is a repeat in x.
                       # A better way is just to find when remainder=1, but I didn't see that initially
        while(numerator<i):
            numerator = numerator * 10
        x.append((numerator%i, numerator/i))
        numerator = x[-1][0]
        if numerator==0:    #number will end in 0 repeating
            cycle=1
            break
        
        for j in range(len(x)-1):
            if x[j]==x[-1]:
                cycle = len(x)-1-j
                break
            
    
    if cycle > longest:
        longestd=i
        longest=cycle
        
print(longestd)