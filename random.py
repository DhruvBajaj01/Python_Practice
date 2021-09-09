#!/usr/bin/env python
# coding: utf-8

# In[22]:


import random
def select(list):
 
  print ("Original list of players : " + str(list)) 
  random_num = random.choice(list) 
  print ("Random selected player is : " + str(random_num)) 

        
        
player = ['Kohli','Tendulkar','Lara','Ponting','Kallis']
select(player)

