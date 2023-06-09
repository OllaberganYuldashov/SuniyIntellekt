from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

iris=load_iris()
#print(iris)

knn = KNeighborsClassifier(n_neighbors=11)
X,y=iris.data,iris.target
knn.fit(X,y)

print(knn.predict([(5,2,5,2)]))

