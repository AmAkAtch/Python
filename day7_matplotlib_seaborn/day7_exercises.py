import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

x = [1,2,3,4]
y= [10,20,25,30]

plt.scatter(x, y, color="red")
plt.show()

array1 = np.array([[1,2],[3,4]])
sns.heatmap(array1)
plt.show()

iris = sns.load_dataset("iris")
sns.pairplot(iris, hue="species")
plt.show()