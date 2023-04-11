import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
kmean=KMeans(n_clusters=3)

x=[9,6,11,10,7,12,2,1,8,10]
y=[15,12,9,4,10,4,3,1,4,1]
data=list(zip(x,y))
kmean.fit(data)
print(kmean.cluster_centers_)

plt.scatter(x,y,c=kmean.labels_)
plt.show()

