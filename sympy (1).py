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


# In[1]:


from sympy import sin,cos
x=int(input())
y=int(input())
print("sin(2x) + cos(2x) = ", (sin(2*x)+cos(2*x)).evalf())
print("\n 3x + y^3 = ", (3*x)+(y**3))


# In[2]:


from sympy import *
print(N(sqrt(2)*1,100))
a_054=Rational(1/2)
b_054=Rational(1/3)
print(a_054+b_054)
x,y,n=symbols('x y n')
exp=expand((x+y)**6)
print(exp)
print(simplify(sin(x)/cos(x)))
print(simplify(sin(x)-x**3*n))


# In[ ]:




