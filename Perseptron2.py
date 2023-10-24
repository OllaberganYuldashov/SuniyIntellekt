import numpy as np
import random as rd

input=np.array([
    [0,0,0],
    [0,0,1],
    [0,1,0],
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1]
])
t=np.array([0,1,1,1,1,1,0,0])

input[input==0]=-1
t[t==0]=-1

w=[rd.randint(0,1) for i in range(3)]
b=rd.randint(0,1)

predicts=[]
def f(net):
    if net>0:
        return 1
    return -1
def predict(x,w,b):
    net=x[0]*w[0]+x[1]*w[1]+x[2]*w[2]+b
    return f(net)

alfa=0.7
for i in range(len(input)):
    y=predict(input[i],w,b)
    #print(i,"-tanlanma")
    while not t[i]==y:
        #w=w+alfa*(t[i]-y)*input[i]
        w=w+alfa*t[i]*input[i]
        b=b+alfa*t[i]

        y = predict(input[i], w, b)
        #print(t[i],y)
    predicts.append(y)

print("Tugadi!!!")
predicts=np.array(predicts)
input[input==-1]=0
t[t==-1]=0
predicts[predicts==-1]=0

print("Wazn koeffitsentlar: ",w)
print("Bias:",b)
print("Target:",t)
print("Natijalar:",predicts)
