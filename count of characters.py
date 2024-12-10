#!/usr/bin/env python
# coding: utf-8

# In[1]:


def count_char(s):
    char_count={}
    for char in s:
        if char.isalpha():
            if char in char_count:
                char_count[char]+=1
            else:
                char_count[char]=1
    return char_count
string=input("enter a string")
dict=count_char(string)
for char,count in dict.items():
    print(f"{char}:{count}")


# In[ ]:





# In[ ]:


disha

