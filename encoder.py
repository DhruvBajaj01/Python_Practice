#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ASCIISentence( str ): 
      
    for i in str: 
      print(chr(ord(i)-30), end = '')
      
      

str = input("Enter a string ")
print("The encoded word is ")
ASCIISentence(str)

