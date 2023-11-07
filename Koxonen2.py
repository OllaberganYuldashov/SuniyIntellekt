import numpy as np


X=np.array([
    [1, 1, 0],
    [0, 0, 0],
    [1, 0, 0],
    [0, 0, 1]
])

w=np.array([ [ np.random.random() for j in range(3)] for i in range(3)])
#print(w)

def dist(x1,x2):
    s=0;
    for i in range(len(x1)):
        s+=(x1[i]-x2[i])**2
    return s

alfa=0.3
predict=[]
for x in X:
    d1=dist(x,w[:,0])
    d2=dist(x,w[:,1])
    d3=dist(x,w[:,2])

    if d1<d2 and d1<d3:
        #1-class yaqin
        w[:,0]=w[:,0]+alfa*(x-w[:,0])
        predict.append(-1)
    elif d2<d1 and d2<d3:
        w[:, 1] = w[:, 1] + alfa * (x - w[:, 1])
        predict.append(0)
    elif d3<d1 and d3<d2:
        w[:, 2] = w[:, 2] + alfa * (x - w[:, 2])
        predict.append(1)

predict=np.array(predict)
print(predict)

