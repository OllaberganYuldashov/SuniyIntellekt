import pandas
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

df = pandas.read_csv("datasets/iris.csv")
d = {'Iris-setosa': 0, 'Iris-versicolor': 1,'Iris-virginica':2}
df['Class'] = df['Class'].map(d)


attributes = ['sepal length', 'sepal width', 'petal length', 'petal width']

X = df[attributes]
y = df['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X_train, y_train)

print(dtree.score(X_test,y_test))
