#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import time
size=10**6
python_list=list(range(size))
numpy_array=np.arange(size)
start_time=time.time()
python_list_result=[x+1 for x in python_list]
end_time=time.time()
python_list_time=end_time-start_time
numpy_array_result=numpy_array+1
end_time=time.time()
numpy_array_time=end_time-start_time
print(f"time taken using python list:{python_list_time:.6f}seconds")
print(f"time taken using numpy array:{numpy_array_time:.6f}seconds")
print(f"numpy is approximately{python_list_time/numpy_array_time:.2f}times faster for this operation:")


# In[ ]:



