import pandas as pd
import numpy as np

d = {'size':[500, 500, 500, 1000, 1000,1000,1500,1500,1500],
	 'age':[0, 20, 40, 0, 20, 40, 0, 20, 40],
	 'price':[1000, 800, 600, 1500, 1300, 1100, 2000, 1800, 1600]}
df = pd.DataFrame(data=d)


from sklearn.linear_model import LinearRegression
X = df[['age','size']]
y= df['price']

clf = LinearRegression()
clf.fit(X,y)
clf.coef_

import statsmodels.formula.api as smf
model1=smf.ols('price~size+age',data=df).fit()
print(model1.summary())