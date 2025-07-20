import matplotlib.pyplot as plt
import numpy as np

#Example1: Single Line plot
array1 = np.array([1,2,5,6,8])
array2 = np.array([3,4,7,8,9])

# plt.plot(array1,array2)
plt.title("Simple Line plot")
plt.xlabel("array1")
plt.ylabel("array2")
# plt.show()


#Example2: Barchart
categorires = ["Apple", "Banana", "Chiku"]
quantity = [1,2,5] #This needs to be numbers

#plt.bar(categorires,quantity) #it will only showchart when the x and y value match
plt.title("Simiple Bar Chart")
plt.xlabel("Categories")
plt.ylabel("quantity")
#plt.show()

#Example3: HIstogram
random_data = np.random.randn(10000) #This basically generates 10000 numbers in standard deviation

# plt.hist(random_data,bins=50) #This will gorup that in 50 bins, like -3 to -2.8 etc.
plt.title("HIstogram Example")
plt.xlabel("Value")
plt.ylabel("frquency")
# plt.show()

#Example4: Scatter plot
x = np.random.rand(1000)
y = np.random.randn(1000) #must be of same size

# plt.scatter(x,y)
plt.title("Scatter Plot Example")
plt.xlabel("X")
plt.ylabel("Y")
# plt.show()

#practice exercise
x = [0,1,2,3]
y = [0,1,4,9]

# plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
# plt.show()

#Example5: subplot
# plt.subplot(1,3,1)
# plt.plot(x,y)
# plt.title("Single Line plot")

# plt.subplot(1,3,3)
# plt.bar(categorires,quantity)
# plt.title("Bar chart")
# plt.show()


#example6: use styles in the plot
# plt.plot(x,y, color="green", linestyle="--", marker="x")
# plt.title("Styled Plot line")
# plt.show()

#Example6: Use legends when needed
x = np.array([0,1,2,3])
y = np.array([0,1,4,9])     
#Got error here because x and y were not numpy arrays, when muyltiplying the y by 2, I it was duplicating the list
plt.plot(x,y, label="line1")
plt.plot(x,y*2, label="Line2")
plt.legend()
plt.show()