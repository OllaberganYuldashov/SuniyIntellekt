import math

import numpy as np

x=np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])
x=x.transpose()
"""
x=np.array([
    [0,0,1,1],
    [0,1,0,1],
])
"""
target=np.array([0,0,0,1])

x[x==0]=-1
target[target==0]=-1

#x=np.array([[-1,-1,1,1],[-1,1,-1,1]])
#target=np.array([-1,-1,-1,1])

w=np.array([np.random.random(), np.random.random()])
b=np.random.random()
y_result=[]

print('trainingdan oldingi qiymatlar')
print(w)
print(b)

def f(net):
    if net>0:
        return 1
    return -1

def output(w,x,b):
    y=np.dot(w,np.array(x).transpose())+b
    return f(y)


alfa=0.7
for i in range(4):
    y = output(w, x[:,i], b)
    error = target[i]-y

    while math.fabs(error)>0.01:
        w = w + alfa * error * x[:,i]
        #w = w + alfa * target[i] * x[:,i]

        b=b+alfa*error
        #b=b+alfa*target[i]

        y = output(w, x[:, i],b)
        error = target[i]-y
        """
        if target[i] == y:
            break
        """
        #print(error)

    y_result.append(y)


print('Training tugadi!!!')
print('w=',w)
print('b=',b)
target[target==-1]=0
y_result=np.array(y_result)
y_result[y_result==-1]=0
print('target=',target)
print('natija=',y_result)






