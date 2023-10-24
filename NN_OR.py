import math

import numpy as np

x=np.array([[0,1,1],[1,0,1]])
target=np.array([1,1,1])

w=np.array([np.random.random(), np.random.random()])
b=np.random.random()
y_result=[]
error_list=[]
print('trainingdan oldingi qiymatlar')
print(w)
print(b)

def sigmoid(net):
    return 1.0/(1+math.exp(-net))

def output(w,x,b):
    y=np.dot(w,np.array(x).transpose())+b
    return sigmoid(y)


alfa=0.7
for i in range(3):
    y = output(w, x[:,i], b)
    error = math.fabs(y - target[i])

    while math.fabs(error)>0.01:
        w = w + alfa * error *  y * (1 - y) * x[:,i]
        #print(w)
        b=b+alfa*error*y*(1-y)
        #print(error*y*(1-y))
        #print(b)
        y = output(w, x[:, i],b)
        error = math.fabs(y-target[i])
        #print('error=',error)

    y_result.append(y)
    error_list.append(error)

print('Training tugadi!!!')
print('w=',w)
print('b=',b)
print('target=',target)
print('natija=',y_result)
print('error=',error_list)


