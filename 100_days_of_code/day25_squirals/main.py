import pandas as pd

squirrel_data = pd.read_csv("day25_squirals/data.csv")

#create list of Colors
colors = squirrel_data["Primary Fur Color"].unique().tolist()
colors.pop(0)
colors[1] = "Red"

#create list of color counts
count = squirrel_data["Primary Fur Color"].value_counts().tolist()


#combine lists in one dataframe
final_data = pd.DataFrame({
    "Fur Color": colors,
    "Count":count
})

#print final data
final_data.to_csv("day25_squirals/final_data.csv")