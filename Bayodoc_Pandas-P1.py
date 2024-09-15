#!/usr/bin/env python
# coding: utf-8

# # For this programming assignment, download the following file and save to your default user folder: http://bit.ly/Cars_file

# ## PROBLEM 1: 
# - Save your file as Surname_Pandas-P1.py
# - Using knowledge obtained from the experiment and demonstrations:
#     - Load the corresponding .csv file into a data frame named cars using pandas
#     - Display the first five and last five rows of the resulting cars.

# In[4]:


# Before starting, make sure to import the pandas library and access it by using the keyword "pd'

import pandas as pd


# In[6]:


# Load the csv file to access the data

data = pd.read_csv("cars.csv")
data


# In[8]:


# The function below extracts the first five rows of the data

first_5 = data.head()
first_5 


# In[10]:


# On the other hand, the function below on the other hand extracts the first five rows of the data

last_5 = data.tail()
last_5 

