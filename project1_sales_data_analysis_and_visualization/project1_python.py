import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

"""
Manager has given task to...
- Load and Clean the data
- Calculate total and average sales
- Visualize sales trends over time
- Find the best-performing month
"""
#Create a funciton to load and clean the data
def load_and_clean_data(filepath:str)->pd.DataFrame:
    """Load and clean csv file from the given file path and return dataframe built from csv"""

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File '{filepath}' not found.")
    
    df = pd.read_csv(filepath)
    #clean the column names
    df.columns = df.columns.str.strip().str.capitalize()    #Remove whitespaces from index names and capitalize the first character of each word
    df["Month"] = df["Month"].astype(str).str.strip()
    
    df=df.dropna(subset=["Sales","Month"])
    #This will drop rows where either sales or Month any of them is empty
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
    #Convert each cell in Sales column to numeric, and if can't throw an error
    df=df.dropna(subset=["Sales"])
    #drop rows where sales couldn't be converted
    return df

#function to calculate total and average from sales column
def calc_total_and_average(df:pd.DataFrame)->tuple[float,float]:
    """calculate total and average in the dataframe and return float"""

    total = df["Sales"].sum()
    average = df["Sales"].mean()
    return total, round(average, 3)

#function to find the best performing month
def best_month(df:pd.DataFrame)->str:
    """find the best month based on sales and return month name as string"""

    return df.loc[df["Sales"].idxmax(), "Month"]
    #df["Sales"].idxmax returns the NAME of the index as loc operates with names of index and columns

    #return df.iloc[df["Sales"].argmax(), df.columns.get_loc("Month")]
    #df["Sales"].argmax() returns the index of max number
    #df.columns.get_loc("Month") returns the index of column labeled "Month"
    #Using both numerical values with iloc to get the accurate cell and returning it which would be string

def plot_chart(df:pd.DataFrame):
    """plot the line chart for the given dataframe"""

    #using matplotlib to visualize the sales
    plt.plot(df["Month"], df["Sales"], marker="o", color="red")
    plt.title("Monthly Sales Comparison")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid(True)
    plt.show()


#Main functions of the class
sales_data = load_and_clean_data("sales_data.csv")
total_sales, average_sales = calc_total_and_average(sales_data)
top_month = best_month(sales_data)

print(f"Total sales: {total_sales}")
print(f"Average sales each month: {average_sales}")
print(f"Best performing Month: {top_month}")

plot_chart(sales_data)


