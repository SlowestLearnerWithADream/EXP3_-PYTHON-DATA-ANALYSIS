#!/usr/bin/env python
# coding: utf-8

# # For this programming assignment, download the following file and save to your default user folder: http://bit.ly/Cars_file

# # Problem 2:
# - Save your file as Surname_Pandas-P2.py
# - Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.
#     - Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
#     - Display the row that contains the ‘Model’ of ‘Mazda RX4’.
#     - How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
#     - Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
#   

# In[4]:


# Import pandas library

import pandas as pd


# In[6]:


# Storing the csv file to a variable, "data".

data = pd.read_csv( "cars.csv" )
data


# ### A. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars:

# In[12]:


# Slice the rows from index 0 to 5(excluded) to get the first 5 rows in the data frame
# Slice the columns from index 0 to 9 (excluded) with an increment or step size of 2 to get the first 5 odd columns in the data frame

odd_columns = data.iloc[0:5, 0:9:2]
odd_columns


# ### B. Display the row that contains the ‘Model’ of ‘Mazda RX4’:

# In[15]:


# We are about to locate the row where the Mazda RX4 belongs in the data frame.
## We used boolean indexing where it prints the row if the expression is satisfied or evaluated 'True'

r_mazda = data.loc[ data["Model"] == "Mazda RX4" ]
r_mazda


# ### C. Display how many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have:

# In[18]:


# Set the locate's, " .loc ", row parameter as the model that we want to obtain, then followed by the corresponding columns we want to extract

Cylinder_Camaro_Z28 = data.loc[ data["Model"] == "Camaro Z28" , ["Model", "cyl"]  ]
Cylinder_Camaro_Z28


# ### D. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

# #### Method 1: Locating Row Index
# 1. Display the individual index of the models to see what rows are we about to extract
# 2. Using the locate keyword, set its row parameter as the index of the models
# 3. Using the locate keyword, set its column parameter to the specifications we want to filter
#    

# In[22]:


# Display row number of Mazda RX4 Wag

car1 = data.loc[data["Model"] == "Mazda RX4 Wag"]
car1


# In[24]:


# Display row number of Ford Pantera L

car2 = data.loc[data["Model"] == "Ford Pantera L"]
car2


# In[26]:


# Display row number of Honda Civic

car3 = data.loc[ data["Model"] == "Honda Civic" ]
car3


# ##### By this time we know that Mazda RX4 Wag is in row 1, Ford Pantera L in row 28, and Honda Civic in row 18

# In[29]:


# We used this format in the row parameter because it does not accept multiple indexing such as:
## data["Model"] = "Mazda RX4 Wag", "Ford Pantera L" , "Honda Civic"
### Because the comma " , " separates the row from column parameter

Cylinder_Gear = data.loc[ [1,18,28] , ["Model", "cyl", "gear"]]
Cylinder_Gear


# #### Method 2: Boolean Indexing
# 1. Use .isin() to check the presence of multiple elements in a data series or frame in a container.
#    - The syntax " .isin() " is derived from the keyword " in " used in for loops, lists, strings, etc.
#    - The " .isin() " function checks the presence of multiple elements in data frames or series to a set of values such as a list.
#    - While, the " in " function can only check the presence of only one element to a set of values.

# In[48]:


# If the ".isin()" expression is satisfied, then it locates the rows of those car models

Cylinder_Gear = data.loc[ data["Model"].isin(["Mazda RX4 Wag", "Ford Pantera L", "Honda Civic"]), ["Model", "cyl", "gear"]]

Cylinder_Gear

