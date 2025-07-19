import pandas as pd
import numpy as np

#Load data
try:
    sales_data = pd.read_csv("sales.csv")
except FileNotFoundError:
    print("Incorrect File Name")
    exit()
    
#convert the sales column to separate array for faster executions using to_numpy()
sales_array = sales_data["Sales"].to_numpy() 

#calculations
total_sales = np.sum(sales_array)
average_sales = np.mean(sales_array)
max_index = np.argmax(sales_array)
max_month = sales_data["Month"].iloc[max_index]

print(f"Total Sales: {total_sales}")
print(f"Average Sales: {average_sales}")
print(f"Highest Sales Month: {max_month}")