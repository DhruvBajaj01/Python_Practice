#!/usr/bin/env python
# coding: utf-8

# In[2]:


def CheckMonotonic(A): 
  
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 
lst = [] 
  

n = int(input("Enter number of elements : ")) 
  

for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) 
      
print("first list entered",lst) 

print(CheckMonotonic(lst)) 
lst1 = [] 
  

n = int(input("Enter number of elements : ")) 
  

for i in range(0, n): 
    ele = int(input()) 
  
    lst1.append(ele) 
      
print("second list entered",lst1) 

print(CheckMonotonic(lst1)) 

