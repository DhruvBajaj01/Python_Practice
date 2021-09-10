#!/usr/bin/env python
# coding: utf-8

# In[66]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings("ignore")


# In[67]:


df= pd.read_csv(r"C:\Users\Dhruv Bajaj\Downloads\blobCity\train_u6lujuX_CVtuZ9i.csv")
df.head(20)


# In[56]:


df.isnull().sum()


# In[23]:


df['LoanAmount'].values


# In[57]:


df['LoanAmount'].fillna(df['LoanAmount'].median(), inplace=True)


# In[58]:


df.isnull().sum()


# In[25]:


df['Gender']


# In[71]:


df['Gender']=LabelEncoder().fit_transform(df['Gender'])
df['Gender']


# In[72]:


df['Gender'] = OrdinalEncoder().fit_transform(df['Gender'].values.reshape(-1, 1))
df['Gender']


# In[70]:


df['Gender']=np.where(df['Gender']=='Male',1,0)
df['Gender']


# In[41]:


df[['ApplicantIncome','CoapplicantIncome']]


# In[42]:


df['sum_column'] = df["ApplicantIncome"] + df["CoapplicantIncome"]
df['sum_column']


# In[43]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
print(scaler.fit(df[['ApplicantIncome','CoapplicantIncome']]))


# In[46]:


print(scaler.transform(df[['ApplicantIncome','CoapplicantIncome']]))


# In[49]:


from sklearn.preprocessing import RobustScaler
transformer = RobustScaler().fit(df[['ApplicantIncome','CoapplicantIncome']])
transformer.transform(df[['ApplicantIncome','CoapplicantIncome']])


# In[50]:


from sklearn.preprocessing import MinMaxScaler

scaler =  MinMaxScaler()

print(scaler.fit(df[['ApplicantIncome','CoapplicantIncome']]))
print(scaler.transform(df[['ApplicantIncome','CoapplicantIncome']]))


# In[53]:


df.groupby('Education', as_index=False).sum_column.mean()


# In[ ]:




