#!/usr/bin/env python
# coding: utf-8

# task 4
# You are given a positive integer . Print a numerical triangle of height  like the one below:
# 
# 1
# 22
# 333
# 4444
# 55555
# ......
# Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.
# 
# Note: Using anything related to strings will give a score of .
# 
# Input Format
# A single line containing integer,

# In[ ]:


for n in range(1,int(input())):
    print(n * (10 ** n - 1) // 9)


# In[ ]:




