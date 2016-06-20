import sys

answers =[0,1]
for i in range(2,100001):
    n=i
    count=0
    while i>1:
        if i%2==0:
            i=int(i/2)
        else:
            i=3*i+1
        count+=1
        if i<n:
            answers.append(answers[i]+count)
            break


for line in sys.stdin:
    numbers = list(map(int,line.split()))
    longest = 0
    for i in range (min(numbers[0:2]),max(numbers[0:2])+1):
        count=0
        while i>100000:
            if i%2==0:
                i=int(i/2)
            else:
                i=3*i+1
            count+=1
        count += answers[i]
        if count > longest:
            longest=count

    print(numbers[0], numbers[1], longest)