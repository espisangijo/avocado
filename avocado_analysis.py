
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr


# In[42]:


city= 'Chicago'


# # Extract data

# In[43]:


'''get data'''
avocado_df = pd.read_csv('avocado.csv', header=0, index_col=1)
humidity_df = pd.read_csv('humidity.csv', header=0, index_col=0)
temperature_df = pd.read_csv('temperature.csv', header=0, index_col=0)


# # Filter data

# In[44]:


# avocado data
avocado = avocado_df['region'] == city
avocado_df1 = avocado_df[avocado].groupby(['Date']).agg('mean')
avocado_df1.index = pd.to_datetime(avocado_df1.index, format='%Y-%m-%d')
avocado_df1 = avocado_df1.loc['2016-01-10':'2017-12-30', :]


# In[45]:


# avocado data
avocado = avocado_df['region'] == city
avocado_df2 = avocado_df[avocado].groupby(['Date']).agg('sum')
avocado_df2.index = pd.to_datetime(avocado_df2.index, format='%Y-%m-%d')
avocado_df2 = avocado_df2.loc['2016-01-04':'2017-12-30', :]


# In[46]:


# humidity data
humidity_df.index = pd.to_datetime(humidity_df.index, format='%d/%m/%Y %H:%M').strftime('%Y-%m-%d')
humidity_df.index = pd.to_datetime(humidity_df.index, format='%Y-%m-%d')
humidity_df = humidity_df[[city]]
humidity_df = humidity_df.loc['2016-01-10':'2017-12-30']
humidity_df = humidity_df.resample('W').mean()


# In[47]:


# temperature data
temperature_df.index = pd.to_datetime(temperature_df.index, format='%d/%m/%Y %H:%M').strftime('%Y-%m-%d')
temperature_df.index = pd.to_datetime(temperature_df.index, format='%Y-%m-%d')
temperature_df = temperature_df[[city]]
temperature_df = temperature_df.loc['2016-01-10':'2017-12-30']
temperature_df = temperature_df.resample('W').mean()


# # Process data

# In[48]:


# interpolation
avocado_df2 = avocado_df2.reindex(humidity_df.index).interpolate(how="linear")


# In[49]:


# interpolation
avocado_df1 = avocado_df1.reindex(temperature_df.index).interpolate(how="linear")


# # Analyze data

# In[50]:


# Correlation between Humidity and Temperature
corr, p_value = pearsonr(humidity_df[[city]], temperature_df[[city]])
print(corr)
print(p_value)


# In[51]:


# Correlation between Avocado Sales and Temperature
corr, p_value = pearsonr(temperature_df[[city]], avocado_df2[['Total Volume']])
print(corr)
print(p_value)


# In[52]:


# Correlation between Avocado Sales and Humidity
corr, p_value = pearsonr(humidity_df[[city]], avocado_df2[['Total Volume']])
print(corr)
print(p_value)


# In[53]:


# Correlation between Humidity and Temperature
corr, p_value = pearsonr(temperature_df[[city]], humidity_df[[city]])
print(corr)
print(p_value)


# In[54]:


# Correlation between Avocado Price and Humidity
corr, p_value = pearsonr(humidity_df[[city]], avocado_df1[['AveragePrice']])
print(corr)
print(p_value)


# In[55]:


# Correlation between Avocado Price and Temperature
corr, p_value = pearsonr(temperature_df[[city]], avocado_df1[['AveragePrice']])
print(corr)
print(p_value)


# In[56]:


# Correlation between Avocado Price and Total Volume
corr, p_value = pearsonr(avocado_df2[['Total Volume']], avocado_df1[['AveragePrice']])
print(corr)
print(p_value)


# In[57]:


avocado_df1['AveragePrice'].plot(style='b.', x_compat=True)
title = 'Avocado Average Price (' + city + ')'
plt.title(title)
plt.ylabel('Average Price')
plt.xlabel('Date')
plt.show()


# In[58]:


temperature_df[city].plot(style='r.', x_compat=True)
title = city + ' Temperature'
plt.title(title)
plt.ylabel('Temperature (K)')
plt.xlabel('Date')
plt.show()


# In[59]:


humidity_df[city].plot(style='g.', x_compat=True)
title = city + ' Humidity'
plt.title(title)
plt.ylabel('Humidity')
plt.xlabel('Date')
plt.show()


# In[60]:


avocado_df1['Total Volume'].plot(style='k.', x_compat=True)
title = 'Avocado Sales Volume (' + city + ')'
plt.title(title)
plt.ylabel('Volume')
plt.xlabel('Date')
plt.show()

