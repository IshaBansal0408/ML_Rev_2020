#!/usr/bin/env python
# coding: utf-8

# # Contour Plots

# In[9]:


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


# In[10]:


a=np.arange(-1,1,0.02) #(min,max,step)
b=a
a,b=np.meshgrid(a,b)


# In[11]:


plt.style.use('dark_background')
fig=plt.figure()
axes = fig.gca(projection='3d')
axes.contour(a,b,a**2+b**2,cmap='rainbow')
plt.show()


# In[ ]:




