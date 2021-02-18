#!/usr/bin/env python
# coding: utf-8

# # Surface Plots

# - Visualise Loss function in ML and DL
# - Visualise state or state value function in Refinforcement Learning

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


# # Data Generation

# In[2]:


a = np.array([1,2,3])
b=np.array([4,5,6,7])


# In[3]:


a,b=np.meshgrid(a,b)


# In[4]:


a #first is repeated in each row b times


# In[5]:


b #second is repeated in each column a times


# # Surface Plotting

# In[6]:


plt.style.use('dark_background')
fig = plt.figure()
axes = fig.gca(projection='3d')
plt.show()


# In[7]:


fig = plt.figure()
axes = fig.gca(projection='3d')
# (x,y,z) where z is the equation of the plane
axes.plot_surface(a,b,a+b)
plt.show()


# In[8]:


fig = plt.figure()
axes = fig.gca(projection='3d')
axes.plot_surface(a,b,a+b,cmap='rainbow') #cmap - color map
plt.show()


# In[9]:


fig = plt.figure()
axes = fig.gca(projection='3d')
axes.plot_surface(a,b,a**2+b**2+30,cmap='rainbow') #cmap - color map
plt.show()


# # Data Generation - II

# In[10]:


a=np.arange(-1,1,0.02) #(min,max,step)


# In[11]:


a


# In[12]:


b=a


# In[13]:


a,b=np.meshgrid(a,b)


# In[14]:


a.shape


# In[15]:


fig = plt.figure()
axes = fig.gca(projection='3d')
axes.plot_surface(a,b,a**2+b**2,cmap='rainbow') #cmap - color map
plt.show()


# In[ ]:




