import numpy as np

with open('C:/Users/user/Desktop/ProjectEuler/list.txt','r') as f:
    x=np.loadtxt(f, dtype='f8')

sum=0
for i in range (0, len(x)):
    sum+=x[i]
print (sum)