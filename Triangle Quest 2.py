#!/usr/bin/env python
# coding: utf-8

# task 3
# You are given a positive integer N.
# Your task is to print a palindromic triangle of size N .
# 
# For example, a palindromic triangle of size 5 is

# In[ ]:


for n in range(1,int(input())+1):
   print(int((10**n-1)/9)**2)


# In[ ]:




