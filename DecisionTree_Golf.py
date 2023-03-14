import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

df = pandas.read_csv("datasets/golf_df.csv")
df.info
d = {'sunny': 0, 'overcast': 1,'rainy':2}
df['Outlook'] = df['Outlook'].map(d)
d = {'hot': -1, 'mild': 0,'cool':1}
df['Temperature'] = df['Temperature'].map(d)
d = {'high': 1, 'normal': 0}
df['Humidity'] = df['Humidity'].map(d)
d = {True: 1, False: 0}
df['Windy'] = df['Windy'].map(d)

d = {'no': 0, 'yes': 1}
df['Play'] = df['Play'].map(d)
print(df)

attributes = ['Outlook', 'Temperature', 'Humidity', 'Windy']

X = df[attributes]
y = df['Play']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

tree.plot_tree(dtree, feature_names=attributes)
plt.show()
