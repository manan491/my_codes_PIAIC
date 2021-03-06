#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[1]:


import numpy as np
a = np.array([0,1,2,3,4,5,6,7,8,9])
a = a.reshape(2,5)


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# In[2]:


a= np.array([[0,1,2,3,4],[5,6,7,8,9]])
b= np.array([[1,1,1,1,1],[1,1,1,1,1]])
np.vstack((a,b))


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[3]:


a= np.array([[0,1,2,3,4],[5,6,7,8,9]])
b= np.array([[1,1,1,1,1],[1,1,1,1,1]])
np.hstack((a,b))


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[4]:


a = np.array([[0,1,2,3,4],[5,6,7,8,9]])
a = a.flatten()
a


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[5]:


b = np.array([[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14]])
b = b.flatten()
b


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[6]:


c = np.array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
c = c.reshape(5,3)


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[7]:


f = np.arange(25).reshape(5,5)
np.square(a)


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[8]:


g = np.arange(30).reshape(5,6)
g.mean()


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[9]:


g.std()


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[10]:


np.median(g)


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[11]:


np.transpose(g)


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[12]:


h = np.arange(16).reshape(4,4)
np.diag(h).sum()


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[13]:


np.linalg.det(h)


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[14]:


a = np.random.randn(100)
print(np.percentile(a,5))
print(np.percentile(a,95))


# ## Question:15

# ### How to find if a given array has any null values?

# In[19]:
arr = np.arange(15).reshape(-1,3)
array_sum = np.sum(arr)
array_has_nan = np.isnan(array_sum)
array_has_nan


