import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

iris=pd.read_csv('datasets/iris.csv')

d = {'Iris-setosa': 0, 'Iris-versicolor': 1,'Iris-virginica':2}
iris['Class'] = iris['Class'].map(d)

attributes = ['sepal length', 'sepal width', 'petal length', 'petal width']

X = iris[attributes]
y = iris['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

knn = KNeighborsClassifier(n_neighbors=11)
knn.fit(X_train,y_train)
print(knn.score(X_test,y_test)*100)