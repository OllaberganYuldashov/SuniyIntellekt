from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt
import  numpy as np


#x=[45,23,66,32,73,50,40,25,32,62] #Area
#x=[2,3,4,3,7,5,4,2,6,3] #level
x=[2,1,3,1,3,2,2,1,2,2]
y=[535,210,745,320,800,420,390,250,300,400]

plt.scatter(x,y)
plt.show()

x=pd.DataFrame(x)
y=pd.DataFrame(y)


l_reg=linear_model.LinearRegression()
l_reg.fit(x,y)

print(l_reg.coef_)
print(l_reg.intercept_)
print(l_reg.predict(np.array([[32]])))
