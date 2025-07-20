import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#example1: Boxplot
data = pd.DataFrame({"Category":["A","A","B","B"], "value":[10,15,20,25]})
# sns.boxplot(x="Category",y="value",data=data)
# plt.show()

#example2: Heatmap
corr = np.corrcoef(np.random.rand(10,10))
# sns.heatmap(corr, annot=True)
# plt.show()

#example3: PairPLot
iris = sns.load_dataset("iris")

# sns.pairplot(iris, hue="species")
# plt.show()


#example4: Load Seaborn's "tips" dataset and make box of total bills by day
tips = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Total Bill Distribution by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()
