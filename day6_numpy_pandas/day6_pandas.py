import pandas as pd
"""
pandas has 2 key structures
 1. Series: a labeled 1d array like a single column
 2. Dataframe : a 2d table with rows and columns
"""

#Example1: Creating Series
data = [10, 20, 30]
series = pd.Series(data)
print(series)
#prints the converted list in tabular formate with extra column as index

#Example2: Creating dataframe
data = {
    "Name":["Alice", "Bob", "Charlie"],
    "Age":[20, 30, 25]
}
print(data["Name"])
df = pd.DataFrame(data)
print(df)


#Example4: reading csv file
dataFile = pd.read_csv("data.csv")
print(dataFile)
#functions that can be performed with data
print(dataFile.info())      #shows the information about the dataframe
print(dataFile.head(1))     #Shows only the number of rows mentioned here
print(dataFile.describe())  #Show stats for numbers in dataframe

#Example5: Accessing the specific columns and rows
ages = dataFile["Age"]      #Access columns using like objects
ages = dataFile.Name        
print(ages)

first_column = dataFile.iloc[1]     #access the specific row using the row number
print(first_column)


#Example 6: Modifying the data
dataFile["Country"] = "USA" #Creates a new column if cant find one and adds the default value to every row
print(dataFile)
dataFile.at[0,"Age"] = 26 #Changing the specifc row and column
print(dataFile)

"""
Best practices to for pandas
- Use dataFile.dropna() to remove the missing rows or dataFile.fillna(value) to fill them
- use pandas built-in methods for speed in stead of looping on the data
"""