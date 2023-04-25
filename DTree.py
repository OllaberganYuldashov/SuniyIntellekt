import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

x=[[46],[65],[68],[69],[70],[71],[72],[74],[75],[75],[80],[81],[83],[85]]
y=[1,0,0,0,0,1,1,1,1,1,1,0,0,0]

dtree = DecisionTreeClassifier(max_depth=1, criterion='entropy')
dtree = dtree.fit(x, y)

tree.plot_tree(dtree, feature_names='x')
plt.show()


