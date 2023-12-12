import math
import random as rd
import numpy as np
import warnings

warnings.filterwarnings('ignore')

X=np.array([
        [0,0],
        [0,1],
        [1,0],
        [1,1]
])

target=np.array([0,1,1,0])

C=np.array([
        [0,0],
        [0,1],
        [1,0],
        [1,1]
])

sigma=1

def dist(x,c):
    s = 0
    for i in range(len(x)):
        s += (x[i] - c[i]) ** 2
    return math.sqrt(s)

def Gauss(x,c,sigma):
    return math.pow(math.e,-(dist(x,c))/(2*sigma*sigma))

w=np.array([rd.random() for i in range(4)])
#print("w=",w)
def Sigmoid(x):
    x=np.float16(x)
    return 1 / (1 + np.exp(-x))

l_rate=1

def Bacpropagation(fi,t,w):
    #print("w(old): ",w)
    w=np.array(w)
    y=Sigmoid(np.dot(fi,w.transpose()))
    #print("y=",y," t=",t)
    error=(y-t)
    #print("error=",error)
    print("w(old): ", w)
    while math.fabs(error) > 0.01:

        #w = w + l_rate *(1-y)*y* error*fi
        w = w - np.dot(l_rate *(1-y)*y* error,fi)

        y = Sigmoid(np.dot(fi,w.transpose()))
        error = (y-t)

    print("w(new): ", w)
    print(error)
    return w

for j in range(1000):
    for i in range(len(X)):
        fi=[Gauss(X[i],C[j],sigma) for j in range(len(C))]
        print((i+1),"- fi : ",fi)
        w=Bacpropagation(fi,target[i],w)

print(w)

for i in range(len(X)):
    fi=[Gauss(X[i],C[j],sigma) for j in range(len(C))]
    y = Sigmoid(np.dot(fi, w.transpose()))
    y=round(y)

    print("y=",y,"  t=",target[i])



