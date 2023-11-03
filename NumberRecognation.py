#https://medium.com/@borandabak/number-recognition-with-python-939cd8427a43
#https://www.kaggle.com/competitions/digit-recognizer/data?select=sample_submission.csv
#input 1x784     w 784x10    => 1x10

import pandas as pd
import numpy as np

data = pd.read_csv("datasets/train.csv")
#print(data.shape)
w=np.array([[np.random.random() for j in range(10)] for i in range(784)])
b=np.array([np.random.random() for i in range(10)])
#print(w.shape)
label=data['label']
#print(label)
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
data[data>100]=1

def sign(output):
    output=np.array(output)
    output[output>0]=1
    output[output<=0]=-1
    return output

output=np.array([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])

alfa=0.5

for i in range(len(data)):

    output=sign(np.dot(data[i],w)+b)

    while not (np.array_equal(output,target[i])):

        for j in range(10):
            w[:,j]=w[:,j]+alfa*(target[i,j]-output[j])*data[i]

        b=b+alfa*(target[i]-output)
        output = sign(np.dot(data[i], w) + b)


print(w)
np.savetxt(f'weight.txt', w)
np.savetxt(f'bias.txt',b)