
# coding: utf-8

# In[6]:


import os
try:
    os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
except FileNotFoundError:
    path = input('Ваш браузер не хранится в папке "по умолчанию", введите пожалуйста полный путь в формате C:\..\chrome.exe: ')
    os.startfile(path)

