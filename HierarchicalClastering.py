import matplotlib.pyplot as plt1
import numpy as np

X = np.array([[2,2],[3,5],[7,9],[6,15],[3,7],[7,5],[3,8]])
labels = range(1, 8)
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
labelList = range(1, 8)
plt2.figure(figsize=(10, 7))

dendrogram(linked, orientation='top',labels=labelList,
distance_sort='descending',show_leaf_counts=True)
plt2.show()