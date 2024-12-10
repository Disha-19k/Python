#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def __add__(self,other):
        return Complex(self.real+other.real,self.imaginary+other.imaginary)
    def __sub__(self,other):
        return Complex(self.real-other.real,self.imaginary-other.imaginary)
    def __mul__(self,other):
        real_part=(self.real*other.real)-(self.imaginary*other.imaginary)
        imaginary_part=(self.real*other.imaginary)+(self.imaginary*other.real)
        return Complex(self.real*other.real,self.imaginary*other.imaginary)
    def __str__(self):
        return f"{self.real}+{self.imaginary}i"
if __name__=="__main__":
    c1=Complex(2,3)
    c2=Complex(1,4)
    result_add=c1+c2
    print(f"addition:{result_add}")
    result_sub=c1-c2
    print(f"substraction:{result_sub}")
    result_mul=c1*c2
    print(f"multiplication:{result_mul}")
        
    


# In[ ]:



