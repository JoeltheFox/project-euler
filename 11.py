import numpy as np
f = open('Users/joelfox/desktop/projecteuler/matrix.txt','r')
x=np.loadtxt(f, dtype=int)

greatest = 0

#vert
for i in range (0,17):
    for j in range (0,20):
        new=x[i,j]*x[i+1,j]*x[i+2,j]*x[i+3,j]
        if new > greatest:
            greatest=new

#horiz
for i in range (0,20):
    for j in range (0,17):
        new=x[i,j]*x[i,j+1]*x[i,j+2]*x[i,j+3]
        if new > greatest:
            greatest=new
#diagrd
for i in range (0,17):
    for j in range (0,17):
        new=x[i,j]*x[i+1,j+1]*x[i+2,j+2]*x[i+3,j+3]
        if new > greatest:
            greatest=new

#diagru
for i in range (0,17):
    for j in range (0,17):
        new=x[i+3,j]*x[i+2,j+1]*x[i+1,j+2]*x[i,j+3]
        if new > greatest:
            greatest=new
            
print (greatest)