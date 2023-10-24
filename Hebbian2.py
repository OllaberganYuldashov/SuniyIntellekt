import numpy as np

input=np.array([
    [0,1,0,1],
    [1,1,0,1],
    [0,1,1,1],
    [1,1,1,1],
    [0,0,1,0]
])

t=np.array([1,0,0,1,0])


input[input==0]=-1
t[t==0]=-1


w=np.array([0,0,0,0])
b=0
y_result=[]

def f(net):
    if net>0:
        return 1
    return -1

def predict(w,x,b):
    y=np.dot(w,np.array(x).transpose())+b
    return f(y)

for i in range(len(input)):
    for j in range(4):
        w=w+input[i]*t[i]
        b=b+t[i]


for i in range(len(input)):
    y_result.append(predict(w,input[i],b))

print("O`qitish tugadi")
y_result=np.array(y_result)
y_result[y_result==-1]=0
t[t==-1]=0
input[input==-1]=0
print("input:",input)
print("target:",t)
print("predict:",y_result)
print("weight:", w)
print("bais:", b)
