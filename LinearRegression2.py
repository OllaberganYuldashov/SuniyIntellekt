from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt
import  numpy as np


x=[[16,2],[16,3],[8,2],[4,2],[64,3],[8,3]]
y=[80,100,30,20,150,40]


x=pd.DataFrame(x)
y=pd.DataFrame(y)

print(x)
l_reg=linear_model.LinearRegression()
l_reg.fit(x,y)

print(l_reg.coef_)
print(l_reg.intercept_)
print(l_reg.predict(np.array([[32,3]])))
