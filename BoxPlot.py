import matplotlib.pyplot as plt
import numpy as np

data=[12,3,4,5,42,10,32,50]

fig =plt.figure(figsize=(10,3))

plt.boxplot(data,vert=0)
plt.show()