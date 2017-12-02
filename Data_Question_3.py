
# coding: utf-8

# In[119]:


from bs4 import BeautifulSoup as BS
import urllib.request
import pandas as pd
import numpy as np
import re as re


# #### Define url as data frame and read in

# In[62]:


request = urllib.request.Request('https://en.wikipedia.org/wiki/List_of_deadly_earthquakes_since_1900')
result = urllib.request.urlopen(request)
resulttext = result.read()


# #### Use BS constructor to pull data from HTML document 

# In[63]:


soup = BS(resulttext, 'html.parser')


# #### Look at well formed print of your soup

# In[72]:


soup.prettify


# #### Find particular elements in the soup 

# In[82]:


data = []
table = soup.find('table', "sortable wikitable")


# #### You can iterate through your table, grab each row, and pull the < th > and < td > elements into a dataset 

# In[83]:


table = table.find_all('tr')


# In[84]:


for row in table:
    cells = row.find_all('td')
    cells = [ele.text.strip() for ele in cells]
    data.append(cells)


# In[117]:


eq_df = pd.DataFrame(data)
eq_df.drop(0, inplace=True)
###GDP_Market_Prices = GDP_Market_Prices.rename(columns={'Country or Area': 'Country', 'Value': 'GDP'})
eq_df = eq_df.rename(columns={0:'Origin', 1:'Country', 2:'Lat', 3:'Long', 4:'Depth', 5:'Magnitude', 6:'Secondary Effects', 7:'Shaking Deaths', 8:'Total Deaths', 9:'Total Deaths', 10:'EM-DAT Total Deaths', 11: 'Other'})
eq_df = eq_df.apply(lambda x: x.str.strip()).replace('', np.nan)
eq_df.head(1340)

