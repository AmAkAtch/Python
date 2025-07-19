import numpy as np
#First need to install the numpy with pip install numpy command

#example1: numpy array
my_list = [1,2,3,4]
my_array = np.array(my_list)
print(my_list)

#examply2: 2d array
my_2d_array= np.array([[1,2],[3,4]])
#my_test_array=np.array([[1,2],[3]]) ->  This will give array because of the inhomogenous shape
print(my_2d_array)
#creates a 2d array: with 2 columns
print(my_2d_array.shape)    #gives (2,2), which is the shape of the array
print(my_2d_array.dtype)    #gives int64, type of the array


#example3: perform math on entire array without loop
array1 = np.array([1,2,3])
array2 = np.array([5,5,6])

sum_array = array1 + array2 #array type and shape must match in order to perform direct actions
sum_array = array1 + 3 #or you can directly just perform summation with single digits
double_array = sum_array*2 #multiply each number with 2
print(sum_array)
print(double_array)


#example4: useful numpy functions
zeros = np.zeros((2,2)) #Get the array of zeros with 2 colums and 3 rows
ones = np.ones((4,3))
sequence = np.arange(0,10,2) #get the array of sequence starts at 0 (including) and ends at 10(not included) with increment of 2
print(zeros)
print(ones)
print(sequence)

#example5: practice numpy
sequence = np.arange(1,6,1)
sequence = sequence*3
print(sequence)