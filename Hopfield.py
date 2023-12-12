import numpy as np

p=np.array([
    [1,0,1],
    [0,1,0],
    [1,0,1]
])

p=np.reshape(p,(1,9))
p=np.array(p)
pt=np.array(np.reshape(p,(9,1)))
w=np.dot(pt,p)

#print(w)

for i in range(len(w)):
    for j in range(len(w[i])):
        if i==j:
            w[i][j]=0

#print(w)

x=np.array([1,0,0,0,0,0,1,0,0])


def step(y):
    y=np.array(y)
    y[y>0]=1
    y[y<0]=0
    return y

k=0
y=np.array(x.copy())
while not np.array_equal(y,p[0]):
    k+=1
    y=step(np.dot(y,w))
    print(k)
    print(y)

print(k)
