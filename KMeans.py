import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
kmean=KMeans(n_clusters=3)

x=[14,12,6,5,4,9,13,9,3,1]
y=[6,7,4,8,2,5,12,12,1,10]
data=list(zip(x,y))
kmean.fit(data)
print(kmean.cluster_centers_)

plt.scatter(x,y,c=kmean.labels_)
plt.show()

