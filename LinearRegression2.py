from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt
import  numpy as np

#Area level
#x=[[45,2],[23,3],[66,4],[32,3],[73,7],[50,5],[40,4],[25,2],[32,6],[62,3]]
#Area room
x=[[45,2],[23,1],[66,3],[32,1],[73,3],[50,2],[40,2],[25,1],[32,2],[62,2]]

y=[535,210,745,320,800,420,390,250,300,400]


x=pd.DataFrame(x)
y=pd.DataFrame(y)

print(x)
l_reg=linear_model.LinearRegression()
l_reg.fit(x,y)

print(l_reg.coef_)
print(l_reg.intercept_)
print(l_reg.predict(np.array([[32,3]])))
