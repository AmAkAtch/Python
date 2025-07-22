import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#scikit works best with numerical data or dataFrames

#Example1: Linear Regression - It is a teechinque to predict nu bers based on other number
"""Step 1: Load and prepare Data"""
sales_data = pd.read_csv("advertising.csv")
 #if there are missing values, it will be filled with the average of the column

X = sales_data[["Ad_Spend"]].values     #Creates 2D array
Y = sales_data["Sales"].values          #1D series
#X is input array and, Y is output -> X is 2d, Y is 1d

"""Split the data into Training and Testing"""
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
#test_size = 0.2 -> Splits the data in 20% test, and 80% train
#random_state ensures repoducibility meaning everytime you mention the random_state=42, it would make the same split and shuffle

"""Train the model"""
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, Y_train)
#fit() adjusts the model to minimizw prediciton errors

"""Make predictions"""
Y_pred = model.predict(X_test)

"""Evaluate the model"""
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(Y_test, Y_pred)
rmse = np.sqrt(mse)
print(f"mean squared Error: {rmse:.2f}")
#Measure average squared difference between actual and predicated Sales -> Lower is better

"""Visualize the Results"""
plt.scatter(X_test, Y_test, color = "blue", label = "Actual")
plt.plot(X_test, Y_pred, color="red", label = "Predicted")
plt.xlabel("Ad_Spend")
plt.ylabel("Sales")
plt.title("Sales prediction vs actual")
plt.show()



