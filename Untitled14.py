#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
max_temp = np.array ([39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25])
min_temp = np.array([21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18])
months = np.arange(12)
plt.plot(months,max_temp,'ro')
plt.plot(months,min_temp,'bo')
plt.xlabel('Month')
plt.ylabel('Min and Max Temperatures')


# In[2]:


url = 'https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
titanic = pd.read_csv(url)
titanic.head()


# In[3]:


males = titanic[titanic['sex']=='male'].index.value_counts().count()
print("male count is {}".format(males))
females =titanic[titanic['sex']=='female'].index.value_counts().count()
print("female count is {}".format(females))


# In[4]:


list_1 = [males,females]
gender = ['male','female']
colors = ['b','y']
plt.pie(list_1,labels=gender,colors=colors,startangle=90,autopct='%.1f%%')
plt.show()


# In[5]:


male = titanic[titanic['sex']=='male']
female = titanic[titanic['sex']=='female']
fig = plt.figure(figsize=(18,5))
plt.plot(male.fare, male.age, '.b', label='Male')
plt.plot(female.fare, female.age, '.r', label='Female')
plt.axis('equal')
plt.xlabel('Fare')
plt.ylabel('Age')
leg = plt.legend()


# In[ ]:




