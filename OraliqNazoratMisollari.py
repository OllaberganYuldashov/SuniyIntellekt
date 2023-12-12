import numpy as np
import random as rd

w1=np.array([[rd.randint(-2,3) for j in range(2)] for i in range(3)])
print('w1=',w1)

w2=np.array([rd.randint(-2,3) for i in range(3)])
print('w2=',w2)

def sign(x):
    x=np.array(x)
    x[x>0]=1
    x[x<=0]=-1
    return x
def linear(x):
    x = np.array(x)
    x[x <= 0] = 0
    return x

def step(x):
    x = np.array(x)
    x[x > 0] = 1
    x[x <= 0] = 0
    return x

x=np.array([
    [rd.randint(-3,4)],
    [rd.randint(-3,4)]
])

print('x=',x)

#y1=linear(np.dot(w1,x))
#y1=step(np.dot(w1,x))
y1=sign(np.dot(w1,x))

print("y1=",y1)

#y2=linear(np.dot(w2,y1))
#y2=step(np.dot(w2,y1))
y2=sign(np.dot(w2,y1))
print("y2=",y2)

