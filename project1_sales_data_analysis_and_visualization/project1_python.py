import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""
Manager has given task to...
- Load and Clean the data
- Calculate total and average sales
- Visualize sales trends over time
- Find the best-performing month
"""

#Load the CSV file
sales_data = pd.read_csv("sales_data.csv")

#convert sales column to numpy for math operations
only_sales = np.array(sales_data.Sales)

#calculating total and averages
total_sales = np.sum(only_sales)
average_sales = np.mean(only_sales)

print(f"Tatal sales: {total_sales}")
print(f"Average sales each month: {round(average_sales, 3)}")


#using matplotlib to visualize the sales
plt.plot(sales_data["Month"], sales_data["Sales"])
plt.bar(sales_data["Month"], sales_data["Sales"])
plt.title("Monthly sales comparision")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


#Find the best performing month
#get the index first and than use iloc on actual data to get the row
max_sales_index = np.argmax(only_sales)
best_month = sales_data.iloc[max_sales_index, sales_data.columns.get_loc("Month")]
print(f"Best performing Month: {best_month}")
