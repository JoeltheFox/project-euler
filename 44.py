""" This program solves ProjectEuler problem 44, which asks the following:
If pentagonal numbers are of the form n(3n-1)/2, find the difference D
between the pair of numbers P1 and P2 that minimize D and satisfies:
P1 and P2 are pentagonal, and so is their sum and their difference.

My first program was too slow, but found a pair satisfying the condition which had
a difference of just under 6,000,000 (but couldn't say it was the smallest).
This improved program uses the fact that the answer cannot be > 6 million.

The algorithm starts out by computing a list of pentagonals that is sufficiently
long, as well as a set of pentagonals which can be used to check if a number is
pentagonal, and which goes high enough to contain sums of pentagonals.

After this, the list of pentagonals is searched for pairs satisying
the criteria, only checking pairs with difference < 6 million.
After all pairs are checked, the lowest difference is reported.

runs in ~10 seconds on my computer"""

pentagonals = [1,5,12]
pentset = {1,5,12}
answer = 0

i=4
y=4
last = 12
Upper_bound = 6000000

while (True):   # This first loop generates the list and set of pentagonals
    pentagonals.append(int(i*(3*i-1)/2))
    
    while last <= (pentagonals[-2]+pentagonals[-1]):
        last = int(y*(3*y-1)/2)
        pentset.add(last)
        y+=1
        
    if pentagonals[-1]-pentagonals[-2] > Upper_bound:
        break
    
    i+=1

for j in range(len(pentagonals)-1):   # This loop checks all pairs with difference <6,000,000 and saves candidate answers
    k=j+1
    while(pentagonals[k]-pentagonals[j]< Upper_bound):
        if int(pentagonals[k]-pentagonals[j]) in pentset and int(pentagonals[k]+pentagonals[j]) in pentset and (answer==0 or (pentagonals[k]-pentagonals[j])<answer):
            answer = int(pentagonals[k]-pentagonals[j])
        if k ==len(pentagonals)-1:
            break
        k+=1
            

print(answer)
