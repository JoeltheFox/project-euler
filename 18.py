x = []
y=[]
for i in range (0,15):
    x.append([])
    y.append([])

with open('C:/Users/user/Desktop/ProjectEuler/triangle.txt','r') as f:
    for i in range (0,15):
        x[i]=(f.readline().split())

y[0]=75
y[1]=[170, 139]
for i in range (2,15):
    for j in range (0,i+1):
        if j==0:
            y[i].append(y[i-1][j]+int(x[i][j]))
        elif j==i:
            y[i].append(y[i-1][j-1]+int(x[i][j]))
        else:
            y[i].append(max(y[i-1][j-1],y[i-1][j])+int(x[i][j]))
            
print (max(y[14]))