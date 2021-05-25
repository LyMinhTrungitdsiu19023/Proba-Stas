import matplotlib

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

# Load CSV and columns
df = pd.read_csv("sulfur_dioxide.csv")

Y = df['free sulfur dioxide'].values.reshape(-1, 1)
X = df['total sulfur dioxide'].values.reshape(-1, 1)

plt.title('Sulfur Dioxide')
plt.xlabel('Total')
plt.ylabel('Free')
plt.xticks(())
plt.yticks(())


linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X, Y)  # perform linear regression
Y_pred = linear_regressor.predict(X)  # make predictions 


plt.scatter(X, Y)
plt.plot(X, Y_pred, color='red')
plt.show()