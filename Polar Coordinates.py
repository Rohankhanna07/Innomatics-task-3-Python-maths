#!/usr/bin/env python
# coding: utf-8

# task 1
# Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.
# 
# A complex number z
# z=x+yi is completely determined by its real part x and imaginary part y.
# Here, j is the imaginary unit.
# A polar coordinate (r,theta) is completely determined by modulus  and phase angle (r,theta)
# Task
# You are given a complex . Your task is to convert it to polar coordinates.

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
num = complex(input())
x = complex(num)

print(cmath.polar(x)[0])
print(cmath.polar(x)[1])


# In[ ]:




