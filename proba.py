import random as rd
import  numpy as np
a=[rd.random() for i in range(10)]

c=np.array([[rd.randint(0,1) for j in range(10)] for i in range(15)])
#print(c)


b=[]
for i in range(10):
    b.append(rd.randint(0,1))



d=np.array([[ (0,0) if i==j else (i,j) for j in range(10)]for i in range(10)])
print(d)
