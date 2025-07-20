import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales.csv")
print(df)

#line plot with matplotlib
plt.plot(df.Month, df.Sales)
plt.title("Simple Line chart for Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

#seaborn bar cahrt
sns.barplot(x="Month", y="Sales", data=df)  #x and y names must match the names of heading in dataFrame
plt.title("MOnthly sales Comparision")
plt.show()