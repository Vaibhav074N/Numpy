"""
1.Numpy is a foundational package for numerical computing in python.

2.ndarray, an efficient multidimensional array providing fast array oriented    arithmetic operations and flexible broadcasting capabilities.

3.mathematical functions for fast operations on entire arrays of data without having to write a loop.

4.Numpy based algorithm are generally 10 to 100 times faster than their pure python connter parts, and uses significantly less memory.

"""
# Ex:

# my_list = list(range(1000000))
# print(my_list)

# import numpy as np

# my_arr = np.arange(1000000)                # This is faster than above
# print(my_arr)

'''
The numpy ndarray: A multidimensional array object

it is fast, flexible container for large data sets

Ex:
'''
import numpy as np

# data = np.random.randn(2,3)          #(2,3) means 2 rows and 3 coloumns.
# print(data)

# print(data.shape)
# print(data.dtype)

# Creating ndarrays

# data1=[6,7.5,8,0,1]
# arr1=np.array(data1)
# print(arr1)

# data2=[[1,2,3,4],[5,6,7,8]]
# arr2=np.array(data2)
# print(arr2)
# print(arr2.ndim)

# print(np.zeros(10))

# You can  explicitly convert or cast an array from one dtype to another using ndaarrays astype method.#

# st = np.array(['1.2','9','-0.6'])
# print(st.dtype)

# print(st.astype(float))

# You can also use another arrays dtype attribute #

# int_array = np.arange(10)
# print(int_array)

# c = np.array([.22,.270,.756,.380,.021])
# print(int_array.astype(c.dtype))

# print(int_array.dtype)

# Arithmetics with Numpy arrays #

# arr3 = np.array([[1,2,3],[5,6,7]])
# print(arr3)

# print(arr3*arr3)
# print(arr3+arr3)
# print(1/arr3)
# print(arr3**0.5)

'''Basic indexing and slicing:
1-dimensional arrays are simple; on the surface they act similarly to python list.
'''
# Fancy indexing

# arr4=np.empty((8,4))
# for i in range(8):
#     arr4[i]=i
    
# print(arr4)

# To select out a subset of the rows in a particular order you can simply pass a list.

# print(arr4[[4,0,1,6]])

# arr5=np.arange(36).reshape((9,4))
# print(arr5)

# Transposing Arrays and Swapping Axes #

# arr6=np.arange(15).reshape((3,5))
# print(arr6)

# print(arr6.T)

# Universal Function #

arr7=np.arange(10)
print(arr7)

print(np.sqrt(arr7))
print(np.exp(arr7))
