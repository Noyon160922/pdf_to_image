#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install pdf2image')


# In[1]:


import os
from pdf2image import convert_from_path


# In[2]:


path="input path"
file = os.listdir(path)
j=0
for x in file:
    # print(x)
    # Store Pdf with convert_from_path function
    images = convert_from_path(path+x)
    
    # for i in range(len(images)):
       
          # Save pages as images in the pdf
    images[0].save('save image path'+str(j) +'.jpg', 'JPEG')
    j+=1
print(j)


# In[ ]:





# In[ ]:


from pdf2image import convert_from_path
 
 
# Store Pdf with convert_from_path function
images = convert_from_path('path')
j=1834
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('path'+ str(j) +'.jpg', 'JPEG')
    j+=1
print(j)


# In[ ]:


from pdf2image import convert_from_path
 
 
# Store Pdf with convert_from_path function
images = convert_from_path('path.pdf')
j=0
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('path'+ str(j) +'.jpg', 'JPEG')
    j+=1
print(j)


# In[ ]:




