#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
shutdown = input('Do you want to shutdown your pc : yes/no: ')
if shutdown == 'yes':
    os.system("shutdown /s /t 1")
else:
    print("shutdown was not permitted")


# In[ ]:




