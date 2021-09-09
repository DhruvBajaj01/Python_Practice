#!/usr/bin/env python
# coding: utf-8

# In[4]:


from sympy import *
print(N(sqrt(2)*1,100))
a=Rational(1/2)
b=Rational(1/3)
print(a+b)
x,y,n=symbols('x y n')
exp=expand((x+y)**6)
print(exp)
print(simplify(sin(x)/cos(x)))
print(simplify(sin(x)-x**3*n))


# In[4]:


import sympy as s
a=s.pi
r=a*5*

