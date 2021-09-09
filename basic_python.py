#!/usr/bin/env python
# coding: utf-8

# In[1]:


i=5

def f(arg=i): 
    print(arg)

i= 6
f()


# In[6]:


a = range(5)

b = range(10)
print(zip(a,b))


# In[7]:


def func1(a=2,b=3):
 print(a,'',b)

func1()

func1(3)


# In[8]:


class Car():
  @staticmethod 
  def factor(type):
    if type == "Racecar": 
        return Racecar()
    if type == "Van": 
        return Van ()
    assert 0, "Bad car creation: " + type
    factory = staticmethod(factory)
class Racecar (Car):
    def drive(self): print ("Race Car driving.")

class Van(Car):
    def drive(self): print("Van driving.")

# Create object using factory.

obj = Car.factor("Van")

obj.drive()

