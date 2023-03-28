import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
iris=load_iris()
#print(iris)
knn = KNeighborsClassifier(n_neighbors=11)
X,y=iris.data,iris.target
knn.fit(X,y)

print(knn.predict([(5,2,5,2)]))

from sklearn.model_selection import GridSearchCV

parm_grid={'n_neighbors':np.arange(1,25)}
kns_grid=GridSearchCV(knn,parm_grid,cv=4)
kns_grid.fit(X,y)
print(kns_grid.best_params_,kns_grid.best_score_)



