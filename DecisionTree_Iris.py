import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

df = pandas.read_csv("datasets/iris.csv")
#print(df.describe())
print(df)
d = {'Iris-setosa': 0, 'Iris-versicolor': 1,'Iris-virginica':2}
df['Class'] = df['Class'].map(d)


attributes = ['sepal length', 'sepal width', 'petal length', 'petal width']

X = df[attributes]
y = df['Class']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

tree.plot_tree(dtree, feature_names=attributes)
plt.show()
