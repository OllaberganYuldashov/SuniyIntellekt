import numpy as np
import random as rd

A=['a','b','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','o`','g`','sh','ch','ng']

input=np.array([[1 if j==i else 0 for j in range(len(A))] for i in range(len(A))])
print(input)

target=np.array([1,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0])


input[input==0]=-1
target[target==0]=-1

w=[rd.randint(0,1) for i in range(29)]
b=rd.randint(0,1)

predicts=[]
def f(net):
    if net>0:
        return 1
    return -1
def predict(x,w,b):
    net=np.dot(w,np.array(x).transpose())+b
    return f(net)

alfa=0.7
for i in range(len(input)):
    y=predict(input[i],w,b)
    #print(i,"-tanlanma")
    while not target[i]==y:
        #w=w+alfa*(t[i]-y)*input[i]
        w=w+alfa*target[i]*input[i]
        b=b+alfa*target[i]

        y = predict(input[i], w, b)
        #print(t[i],y)
    predicts.append(y)

print("Tugadi!!!")
predicts=np.array(predicts)
input[input==-1]=0
target[target==-1]=0
predicts[predicts==-1]=0

print("Wazn koeffitsentlar: ",w)
print("Bias:",b)
print("Target:",target)
print("Natijalar:",predicts)
