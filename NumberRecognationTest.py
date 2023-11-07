#https://medium.com/@borandabak/number-recognition-with-python-939cd8427a43
#https://www.kaggle.com/competitions/digit-recognizer/data?select=sample_submission.csv
#input 1x784     w 784x10    => 1x10

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


data = pd.read_csv("datasets/train.csv")
#print(data)
w=np.array([[np.random.random() for j in range(10)] for i in range(784)])
b=np.array([np.random.random() for i in range(10)])
#print(w.shape)
label=data['label']
target=[]
for x in label:
    tmp = [-1.]*10
    #tmp = [0]*10
    tmp[x]=1.
    target.append(tmp)
    #print(tmp,x)
target=np.array(target)

data=data.drop(columns='label')
data=np.array(data)

data[data==0]=-1
data[data>0]=1

X_train, X_test, y_train, y_test = train_test_split(
    data, target, test_size=0.001, random_state=0)

#print(y_test.shape)
def sign(output):
    output=np.array(output)
    output[output>0]=1
    output[output<=0]=-1
    return output

output=np.array([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])

alfa=0.5

for i in range(len(X_train)):

    output=sign(np.dot(X_train[i],w)+b)

    while not (np.array_equal(output,y_train[i])):

        for j in range(10):
            w[:,j]=w[:,j]+alfa*(y_train[i,j]-output[j])*X_train[i]

        b=b+alfa*(y_train[i]-output)
        output = sign(np.dot(X_train[i], w) + b)

count=0
for i in range(len(X_test)):
    output = sign(np.dot(X_test[i], w) + b)
    print(i,'-namuna')
    print("predict: ",output)
    print("target: ",y_test[i])
    if np.array_equal(y_test[i],output):
        count+=1
        print('togri')

print(count/len(y_test)*100,'%')



