import math


def is_prime(x):
    if x%2==0 and x>2:
        return False
    else:
        for i in range (3,int(math.sqrt(x))+1,2):
            if x%i==0:
                return False
    return True

x = [1,3,7,9]
y = [1,2,3,5,7,9]
truncl = {3,7}
truncr = {2,3,5,7}

digits=1
while(True):
    additions= set()
    for k in truncl:
        if len(str(k))==digits:
            for p in y:
                if is_prime(int(str(p)+str(k))):
                    additions.add(int(str(p)+str(k)))
    truncl.update(additions)
    digits+=1
    for k in truncl:
        if len(str(k))==digits:
            break
    else:
        break
    
digits=1
while(True):
    additions= set()
    for k in truncr:
        if len(str(k))==digits:
            for p in x:
                if is_prime(int(str(k)+str(p))):
                    additions.add(int(str(k)+str(p)))
    truncr.update(additions)
    digits+=1
    for k in truncr:
        if len(str(k))==digits:
            break
    else:
        break
    
answers=truncr.intersection(truncl)
    
print (sum(answers)-17)
    
