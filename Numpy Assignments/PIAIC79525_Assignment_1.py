#!/usr/bin/env python
# coding: utf-8

# # **Assignment For Numpy**

# Difficulty Level **Beginner**

# 1. Import the numpy package under the name np

# In[2]:


import numpy as np


# 2. Create a null vector of size 10 

# In[18]:


np.zeros(10)


# 3. Create a vector with values ranging from 10 to 49

# In[19]:


a = np.arange(10,50)


# 4. Find the shape of previous array in question 3

# In[20]:


a.shape


# 5. Print the type of the previous array in question 3

# In[21]:


a.dtype


# 6. Print the numpy version and the configuration
# 

# In[22]:


print(np.__version__)
print(np.show_config())


# 7. Print the dimension of the array in question 3
# 

# In[23]:


a.ndim


# 8. Create a boolean array with all the True values

# In[24]:


b = np.ones(10,dtype = bool)


# 9. Create a two dimensional array
# 
# 
# 

# In[25]:


c = np.array([[2,3]])


# 10. Create a three dimensional array
# 
# 

# In[26]:


d = np.array([[[2,3,4]]])


# Difficulty Level **Easy**

# 11. Reverse a vector (first element becomes last)

# In[27]:


np.flip([1,2,3,4,5,6,7,8,9])


# 12. Create a null vector of size 10 but the fifth value which is 1 

# In[28]:


f = np.zeros(10)
f[5]  = 5


# 13. Create a 3x3 identity matrix

# In[29]:


np.identity(3)


# 14. arr = np.array([1, 2, 3, 4, 5]) 
# 
# ---
# 
#  Convert the data type of the given array from int to float 

# In[30]:


arr = np.array([1, 2, 3, 4, 5])
arr.astype('float64')


# 15. arr1 =          np.array([[1., 2., 3.],
# 
#                     [4., 5., 6.]])  
#                       
#     arr2 = np.array([[0., 4., 1.],
#      
#                    [7., 2., 12.]])
# 
# ---
# 
# 
# Multiply arr1 with arr2
# 

# In[31]:


arr1 = np.array([[1., 2., 3.],[4., 5., 6.]]) 
arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])
arr1*arr2


# 16. arr1 = np.array([[1., 2., 3.],
#                     [4., 5., 6.]]) 
#                     
#     arr2 = np.array([[0., 4., 1.], 
#                     [7., 2., 12.]])
# 
# 
# ---
# 
# Make an array by comparing both the arrays provided above

# In[34]:


arr3 = arr1[arr1>arr2]


# 17. Extract all odd numbers from arr with values(0-9)

# In[38]:


arr[arr%2 !=0]


# 18. Replace all odd numbers to -1 from previous array

# In[39]:


arr[arr%2 !=0] = -1
arr


# 19. arr = np.arange(10)
# 
# 
# ---
# 
# Replace the values of indexes 5,6,7 and 8 to **12**

# In[4]:


arr = np.arange(10)
arr[5:8] = 12


# 20. Create a 2d array with 1 on the border and 0 inside

# In[19]:


b = np.ones((5,5))
b[1:-1,1:-1] = 0


# Difficulty Level **Medium**

# 21. arr2d = np.array([[1, 2, 3],
# 
#                     [4, 5, 6], 
# 
#                     [7, 8, 9]])
# 
# ---
# 
# Replace the value 5 to 12

# In[5]:


arr2d = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
arr2d[1][1] = 12


# 22. arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# 
# ---
# Convert all the values of 1st array to 64
# 

# In[12]:


arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d[0]=64


# 23. Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it

# In[21]:


arr2a = np.array([[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]])
arr2a = arr2a[1]


# 24. Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it

# In[22]:


arr2a = np.array([[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]])
arr2a = arr2a[0]


# 25. Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows

# In[23]:


arr2a = np.array([[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]])
arr2a = arr2a[0:1,3]


# 26. Create a 10x10 array with random values and find the minimum and maximum values

# In[34]:


g = np.random.randn(10,10)
print(np.max(g),np.min(g))


# 27. a = np.array([1,2,3,2,3,4,3,4,5,6]) b = np.array([7,2,10,2,7,4,9,4,9,8])
# ---
# Find the common items between a and b
# 

# In[41]:


a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a,b)


# 28. a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# 
# ---
# Find the positions where elements of a and b match
# 
# 

# In[57]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
result = np. where(a == b)
if len(result) > 0 and len(result[0]) > 0:
    print(result)


# 29.  names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])  data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will**
# 

# In[3]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
data = np.random.randn(7, 4)
data[names != "Will"]


# 30. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will** and **Joe**
# 
# 

# In[4]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
data = np.random.randn(7, 4)
print(data[names !="Will"])
print(data[names !="Joe"])


# Difficulty Level **Hard**

# 31. Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15.

# In[5]:



arr = np.random.randn(1,15).reshape(5,3)
arr


# 32. Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16.

# In[6]:


dara = np.random.randn(1,16).reshape(2,2,4)


# 33. Swap axes of the array you created in Question 32

# In[7]:


dara = np.random.randn(1,16).reshape(2,2,4)
data.T


# 34. Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0

# In[60]:


v = np.arange(10)
v = np.sqrt(v)
np.where(v<0.5,0,v)


# 35. Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays

# In[8]:


a = np.random.randint(12)
b = np.random.randint(12)
np.maximum(a,b)


# 36. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# 
# ---
# Find the unique names and sort them out!
# 

# In[10]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

names = np.unique(names)
names


# 37. a = np.array([1,2,3,4,5])
# b = np.array([5,6,7,8,9])
# 
# ---
# From array a remove all items present in array b
# 
# 

# In[65]:


a = np.array([1,2,3,4,5]) 
b = np.array([5,6,7,8,9])
g = np.setdiff1d(a, b)
g


# 38.  Following is the input NumPy array delete column two and insert following new column in its place.
# 
# ---
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
# 
# 
# ---
# 
# newColumn = numpy.array([[10,10,10]])
# 

# In[70]:


import numpy
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
sampleArray = numpy.delete(sampleArray , 1, axis = 1)
arr = numpy.array([[10,10,10]])
sampleArray = numpy.insert(sampleArray , 1, arr, axis = 1) 
print (sampleArray)


# 39. x = np.array([[1., 2., 3.], [4., 5., 6.]]) y = np.array([[6., 23.], [-1, 7], [8, 9]])
# 
# 
# ---
# Find the dot product of the above two matrix
# 

# In[46]:


x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
np.dot(x,y)


# 40. Generate a matrix of 20 random values and find its cumulative sum

# In[58]:


matr = np.random.randn(20)
matr.cumsum()

