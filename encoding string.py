#!/usr/bin/env python
# coding: utf-8

# In[1]:


str = input("Enter a string :") 
print("The decoded word is :")
for i in str: 
      print(chr(ord(i)-30), end = '')

