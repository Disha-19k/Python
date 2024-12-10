#!/usr/bin/env python
# coding: utf-8

# In[1]:


def recur_sum(n):
    if(n<=1):
        return n
    else:
        return n+recur_sum(n-1)
num=int(input("enter the number"))
if(num<0):
    print("positive number")
else:
    print("the sum is",recur_sum(num))


# In[ ]:




