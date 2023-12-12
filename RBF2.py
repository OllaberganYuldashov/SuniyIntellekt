import pandas
from sklearn.cluster import KMeans
import math
import numpy as np
import random as rd


df=pandas.read_csv('datasets/iris.csv')
attributes = ['sepal length', 'sepal width', 'petal length', 'petal width']

d = {'Iris-setosa': 0, 'Iris-versicolor': 1,'Iris-virginica':2}
df['Class'] = df['Class'].map(d)

X = df[attributes]
target = df['Class']

c=15
kmeans = KMeans(n_clusters=c,n_init="auto")
kmeans.fit(X)
C=kmeans.cluster_centers_


sigma=1

def dist(x,c):
    s = 0
    for i in range(len(x)):
        s += (x[i] - c[i]) ** 2
    return math.sqrt(s)

def Gauss(x,c,sigma):
    return math.pow(math.e,-(dist(x,c))/(2*sigma*sigma))

w=np.array([rd.random() for i in range(c)])
#print("w=",w)
def Sigmoid(x):
    print(x)
    x=np.float32(x)
    return 2 / (1 + np.exp(-x))

l_rate=1

def Bacpropagation(fi,t,w):
    #print("w(old): ",w)
    w=np.array(w)
    y=Sigmoid(np.dot(fi,w.transpose()))
    print("y=",y," t=",t)
    error=(y-t)
    print("error=",error)
    print("w(old): ", w)
    while math.fabs(error) > 0.1:

        #w = w + l_rate *(1-y)*y* error*fi
        w = w - np.dot(l_rate *(1-y)*y* error,fi)
        #print(np.dot(l_rate *(1-y)*y* error,fi))
        y = Sigmoid(np.dot(fi,w.transpose()))
        error = (y-t)
        print("y=", y, " t=", t)
        print("error=", error)

    print("w(new): ", w)
    print(error)
    return w

x1,x2,x3,x4=X['sepal length'],X['sepal width'],X['petal length'],X['petal width']

for i in range(len(x1)):

    row=[x1[i],x2[i],x3[i],x4[i]]
    print(row)

    fi=[Gauss(row,C[j],sigma) for j in range(len(C))]
    print((i+1),"- fi : ",fi)
    w=Bacpropagation(fi,target[i],w)

print(w)


