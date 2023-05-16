from sklearn import linear_model
import pandas as pd
import numpy as np
df = pd.read_csv("datasets/uyjoy.csv")
print(df)
atributes=['Area','Floor','Rooms','Total_Floor']
x=df[atributes]
y=df['Price']

reg=linear_model.LinearRegression()
reg.fit(x.values,y.values)

print('koefitsentlar: ',reg.coef_)
print('ozod had: ',reg.intercept_)
print(int(reg.predict(np.array([[45.0,4,3,8]]))))
