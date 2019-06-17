#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
from bs4 import BeautifulSoup
import markovify
import re
import unicodedata


# In[68]:


read_text = open('aviral_emails.txt', "r")


# In[69]:


txt = read_text.readlines()


# In[70]:


txt = ''.join(txt)


# In[72]:


txt = txt.replace(u'\xa0', u' ')


# In[73]:


text_model = markovify.Text(txt, state_size = 2)


# In[105]:


aviralified_text = '\n'


# In[106]:


# Print ten randomly-generated sentences using the built model
for i in range(10):
    if i == 5:
        aviralified_text = aviralified_text + '\n\n'+ text_model.make_sentence()
    aviralified_text = aviralified_text + text_model.make_sentence()


# In[107]:


print('Dear Abdul, \n' + aviralified_text + '\n\nRegards, \nAviralify_Python')


# In[ ]:





# In[ ]:




