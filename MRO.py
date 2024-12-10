#!/usr/bin/env python
# coding: utf-8

# In[1]:


class A:
    def classmethod(self):
        print(A)
class B(A):
    def classmethod(self):
        print(B)
class C(A):
    def classmethod(self):
        print(C)
class D(B,C):
    pass
d=D()
d.classmethod()
print(D.__mro__)


# In[ ]:




