#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import csv
import os



# In[3]:


data= pd.read_excel("C:/Users/Marie-Alix Baduel/Desktop/Twitterexcel.xls")
data.head()


# In[31]:


data.shape


# In[32]:


data_columns = ["target", "ids", "date", "flag", "user", "text"]
type(data_columns)


# In[7]:


data.tail(200)


# In[6]:


data= pd.read_excel("C:/Users/Marie-Alix Baduel/Desktop/Twitterexcel.xls", names= data_columns)
data.head(200)


# In[35]:


data.shape


# In[36]:


data['user'].describe()


# In[37]:


data['target']


# In[38]:


data.drop(columns=['target'], inplace=True)


# In[39]:


data.head(20)


# In[40]:


data['text'][1]


# In[ ]:




