import pandas
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
df=pandas.read_csv('datasets/iris.csv')
attributes = ['sepal length', 'sepal width', 'petal length', 'petal width']

d = {'Iris-setosa': 0, 'Iris-versicolor': 1,'Iris-virginica':2}
df['Class'] = df['Class'].map(d)

X = df[attributes]
y = df['Class']

kmeans = KMeans(n_clusters=3,n_init="auto")
kmeans.fit(X)
print(kmeans.cluster_centers_)
#print(kmeans.inertia_)
#print(kmeans.feature_names_in_)
#print(kmeans.labels_)
print(kmeans.score(X,y))

plt.scatter(X['sepal width'],X['sepal length'],c=kmeans.labels_)
plt.show()