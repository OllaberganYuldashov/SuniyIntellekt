import numpy as np

p1=np.array([-1,-1,-1,-1])
p2=np.array([-1,1,-1,1])
p3=np.array([-1,1,1,1])
p4=np.array([1,1,1,1])

p=np.array([1,-1,1,1])

w1=np.array([[p1],[p2],[p3],[p4]])

print('w1=',w1)
e=0.1
w2=np.array([[1 if i==j else -e for j in range(len(p1))]for i in range(len(p1))])
#print(w2)
b=np.array([[4],[4],[4],[4]])
print('b=',b)


y1=np.dot(w1,p.transpose())+b
print('y1=',y1)

def linear(x):
    x=np.array(x)
    x[x<0]=0
    return x

def FinalyAcFunction(x):
    x=np.array(x)
    maximal=np.max(x)
    x[x<maximal]=0
    x[x==maximal]=1
    return x

y2=linear(np.dot(w2,y1))
y2_old=y2.copy()
k=0
while True:
    y2 = linear(np.dot(w2, y2_old))
    print("y2(", k, ")=", y2)
    if np.array_equal(y2,y2_old):
        break
    y2_old = y2.copy()
    k+=1
    #print("epoch ",k)

y2=FinalyAcFunction(y2)

index=-1
for i in range(len(y2)):
    if y2[i]>0:
        index=i+1
        break

print(y2)
print("Berilgan namuna", index,"- klassga tegishli")




