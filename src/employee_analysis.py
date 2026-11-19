#!/usr/bin/env python
# coding: utf-8

# 

# # Employee Analysis
# 
# ## Introduction
# This project analyzes employee salary data.
# 
# ## Objectives
# - Read employee data
# - Calculate average salary
# - Find employee cities

# In[7]:


import pandas as pd

df = pd.read_csv("../data/employees.csv")

print(df)


# In[8]:


get_ipython().run_line_magic('pip', 'install pandas')


# In[10]:


import pandas as pd 


# In[11]:


print("pandas installed success")


# In[13]:


df = pd.read_csv("../data/employees.csv")


# In[14]:


print(df)


# In[15]:


average_salary = df["Salary"].mean()

print("Average Salary:", average_salary)


# In[16]:


chennai = df[df["City"] == "Chennai"]

print(chennai)


# In[17]:


get_ipython().run_line_magic('timeit', 'df["Salary"].mean()')


# In[18]:


highest_salary = df["Salary"].max()

print("Highest Salary:", highest_salary)

