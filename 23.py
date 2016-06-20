import math

def SumofDiv(n):
    tot=1
    i=2
    m=n
    while (i**2)<=n:
        if n%i==0:
            count=0
            extra=1
            while n%i==0:
                count +=1
                extra += (i ** count)
                n=n/i
            tot=tot*extra
        if i==2:
            i=3
        else:
            i=i+2
    if n>1:
        tot=tot*(n+1)
    return int(tot-m)


x=[]
y=[]
for i in range (1,28124):
    for k in x:
        if (i-k) in x:
            break
    else:
        y.append(i)
    if SumofDiv(i)>i:
        x.append(i)
        
print (sum(y))