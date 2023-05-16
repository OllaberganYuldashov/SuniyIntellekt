from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt
import  numpy as np


x=[[2,3],[3,3],[4,2],[6,1],[1,6],[2,4]]
y=[2,3,5,4,2,3]


x=pd.DataFrame(x)
y=pd.DataFrame(y)

print(x)
l_reg=linear_model.LinearRegression()
l_reg.fit(x,y)

print(l_reg.coef_)
print(l_reg.intercept_)
print(l_reg.predict(np.array([[10,3]])))
