#!/usr/bin/env python
# coding: utf-8

# In[1]:


def create_dictionary(words):
    dictionary={}
    for word in words:
        if word:
            first_char=word[0].upper()
            if first_char not in dictionary:
                dictionary[first_char]=[]
        dictionary[first_char].append(word)
    return dictionary
words=input("enter list of words seperated by spaces:").split()
result=create_dictionary(words)
for key,value in sorted(result.items()):
    print(f"{key}:{value}")


# In[ ]:




