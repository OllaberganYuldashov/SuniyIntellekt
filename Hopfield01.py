import numpy as np

p1=np.array([[1,-1,1,-1,1,-1,1,-1,1]])
pt1=np.array(np.reshape(p1,(9,1)))

p2=np.array([[-1,1,-1,1,-1,1,-1,1,-1]])
pt2=np.array(np.reshape(p2,(9,1)))



w=np.dot(pt1,p1)+np.dot(pt2,p2)

#print(w)

for i in range(len(w)):
    for j in range(len(w[i])):
        if i==j:
            w[i][j]=0

#print(w)

#x=[
#    [1,1,1]
#    [0,1,0]
#    [1,1,0]
# ]

x=np.array([1,1,1,-1,1,-1,1,1,-1])


def step(y):
    y=np.array(y)
    y[y>0]=1
    y[y<0]=-1
    return y

k=0
y=np.array(x.copy())
while True:
    k+=1
    y=step(np.dot(y,w))
    if np.array_equal(y,p1[0]):
        print('1-namuna')
        break
    if np.array_equal(y,p2[0]):
        print('2-namuna')
        break

print('Takrorlanishlar soni: ',k)
print(y)
