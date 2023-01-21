#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x = 2
print(x)


# In[ ]:


# Define a dataframe. Then access an element specified by column name and row number
import pandas as pd
df = pd.DataFrame({'Country':["India","Nepal","Pakistan"],'Population':[20,5,10]})
print(df)
df['Country'][2]

nrow = len(df)
print(nrow)

for i in range(nrow):
    print(i)


# In[18]:


# getting the current datetime and then converting it to ISO format
from datetime import datetime
x = datetime.now()

print(x)
x.isoformat()
type(x)


# In[9]:


# specifying a datetime and then converting it to ISO format
from datetime import datetime
dt = datetime(2021, 10, 24, 8, 48, 34, 685496)
print(dt)
print(type(dt))
dt_iso = dt.isoformat()
print(dt_iso)


# In[21]:


from datetime import datetime
x = datetime(1995,8,29,
             12,30,24,943587)
print(x)
y = x.isoformat()
print(y)


# In[24]:


from datetime import datetime
#x = datetime(29-Aug-1995)
#print(x)
y = '29-Aug-1995'
print(y)
datetime(y)

