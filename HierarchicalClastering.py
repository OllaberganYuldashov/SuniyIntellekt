import matplotlib.pyplot as plt1
import numpy as np

X = np.array([[9,15],[6,12],[11,9],[10,4],[7,10],[12,4],[2,3],[1,1],[8,4],[10,1]])
labels = range(1, len(X)+1)
plt1.figure(figsize=(10, 7))
plt1.subplots_adjust(bottom=0.1)
plt1.scatter(X[:,0],X[:,1], label='True Position')
for label, x, y in zip(labels, X[:, 0], X[:, 1]): 
 plt1.annotate(label,xy=(x, y), xytext=(-1, 1),textcoords='offset points',
ha='right', va='bottom')
plt1.show()

from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt2
linked = linkage(X, 'single')
labelList = range(1, len(X)+1)
plt2.figure(figsize=(10, 6))

dendrogram(linked, orientation='top',labels=labelList,
distance_sort='descending',show_leaf_counts=True)
plt2.show()