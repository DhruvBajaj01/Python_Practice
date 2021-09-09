#!/usr/bin/env python
# coding: utf-8

# In[20]:


def unique(list1): 
  
    
    unique_list = [] 
      
  
    for x in list1: 
        
        if x not in unique_list: 
            unique_list.append(x) 
   
    for x in unique_list:  
         print(x, end=" ")
      
list1 = ['cpp','c','python','cpp','java','java']
print("The values of list is")
print(list1)
print("The unique values from  list is") 
unique(list1) 
  


# In[ ]:




