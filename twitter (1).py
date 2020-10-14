#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import csv
import os




# In[8]:


data=pd.read_excel("C:\\Users\\audec\\Documents\\M2\\M2_S1\\Initiation_Python\\Data\\Twitterexcel.xls")
data.head()


# In[9]:


data.shape


# In[10]:


data_columns = ["target", "ids", "date", "flag", "user", "text"]
type(data_columns)


# In[11]:


data.tail(10)


# In[13]:


data= pd.read_excel("C:\\Users\\audec\\Documents\\M2\\M2_S1\\Initiation_Python\\Data\\Twitterexcel.xls", names= data_columns)
data.head(10)


# In[21]:


data.shape

data['user'].describe()


# In[25]:


# on regarde les différentes modalités de target et flag, afin d'évaluer 
#si ce sont des variables discriminantes pertinentes


# In[26]:


data['target'].unique()


# In[ ]:


data['flag'].unique()


# In[ ]:





# In[15]:


data['target']

data.drop(columns=['target'], inplace=True)


# In[18]:


data.head(10)


# In[ ]:





# In[17]:


data['text'][1]


# In[19]:


data['flag']

data.drop(columns=['flag'], inplace=True)


# In[20]:


data.head()


# In[ ]:




