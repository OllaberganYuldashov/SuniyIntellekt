import pandas
from sklearn.model_selection import train_test_split
import numpy as np


df = pandas.read_csv("datasets/iris.csv")
#print(df.describe())
#print(df)
d = {'Iris-setosa': 0, 'Iris-versicolor': 1,'Iris-virginica':2}
df['Class'] = df['Class'].map(d)


attributes = ['sepal length', 'sepal width', 'petal length', 'petal width']

X = df[attributes]
y = df['Class']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.01, random_state=0)

w = np.array([[np.random.random() for j in range(3)] for i in range(4)])

def dist(x1, x2):
    s = 0
    for i in range(len(x1)):
        s += (x1[i] - x2[i]) ** 2
    return s

alfa = 0.5
predict = [-1] * len(y_train)

for j in range(10000):
    i = 0
    for x in X_train:
        d1 = dist(x, w[:, 0])
        d2 = dist(x, w[:, 1])
        d3 = dist(x, w[:, 2])

        _min = min(d1, d2, d3)

        if _min == d1:
            # 1-class yaqin
            w[:, 0] = w[:, 0] + alfa * (x - w[:, 0])
            predict[i] = 0
        elif _min == d2:
            w[:, 1] = w[:, 1] + alfa * (x - w[:, 1])
            predict[i] = 1
        elif _min == d3:
            w[:, 2] = w[:, 2] + alfa * (x - w[:, 2])
            predict[i] = 2
        i += 1

print(w)



