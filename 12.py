import math

def num_div(x):
    num=1
    i=1
    while x>1:
        i+=1
        k=1
        while x%i==0:
            x=x/i
            k+=1
        num=num*k
    return num
    
tria = [1]
while num_div(tria[-1])<501:
    tria.append(tria[-1]+len(tria)+1)
    
print (tria[-1])