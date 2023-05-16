from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt
import  numpy as np


x=[2,3,4,6,1,2]
y=[2,3,5,4,2,3]

plt.scatter(x,y)
plt.show()

x=pd.DataFrame(x)
y=pd.DataFrame(y)


l_reg=linear_model.LinearRegression()
l_reg.fit(x,y)

print(l_reg.coef_)
print(l_reg.intercept_)
print(l_reg.predict(np.array([[10]])))
