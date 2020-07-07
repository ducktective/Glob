#!/usr/bin/env python
# coding: utf-8

# ## 1. Читаем Excel файл

# In[2]:


import numpy as np
import pandas as pd
dataframe = pd.read_excel('for_second_ex.xlsx')


# In[38]:


dataframe.head()


# ## 2. Создаем Dataframe с определенными колонками

# In[7]:


Dataframe = dataframe[['Commodity', 'Region', 'Company', 'Plant No.','Expected Annual Capacity Change (kt)','Total Annual Capacity (kt)']]


# In[5]:


Dataframe.head()


# ## 3. Выводим все строки, где Expected Annual Capacity Change >= Total Annual Capacity 

# In[9]:


filter_1 = Dataframe['Expected Annual Capacity Change (kt)'] >= Dataframe['Total Annual Capacity (kt)']
Dataframe.loc[filter_1]


# In[14]:


a = Dataframe['Expected Annual Capacity Change (kt)']
b = Dataframe['Total Annual Capacity (kt)']
Dataframe.query('@a > = @b')


# ## 4. Вывести первые 4 столбца dataframe и первые 50 строк

# In[34]:


dataframe.iloc[:50,0:3]


# ## 5 Вывести количество строк где:  
#   5.1. Plant No. = 1  

# In[25]:


len(Dataframe.loc[Dataframe['Plant No.'] == 1])


# 5.2. Region = NORTHEAST ASIA

# In[28]:


len(Dataframe.loc[Dataframe['Region'] == 'NORTHEAST ASIA'])


# ## 6. Заменить все значения HDPE в колонке Commodity на HIGH DENSITY POLYETHYLENE, сохранить данные изменения.

# In[36]:


dataframe['Commodity'] = dataframe['Commodity'].replace('HDPE', 'HIGH DENSITY POLYETHYLENE')
dataframe


# In[42]:


dataframe.to_excel('for_second_ex.xlsx')#это я так назвал exel файл

