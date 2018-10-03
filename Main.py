
# coding: utf-8

# In[1]:


import os
import pandas as pd 

path = os.path.join(os.getcwd(), 'Migrations')
print(path)
os.chdir(path)
dir_work = os.listdir(path)
a = len(dir_work)
print(a)  


# In[ ]:


just_massive = []
rez_massive = []
cnt = 0
first_input = input('Введите строку: ')
for i in dir_work:
    check = i.split('.')
    if check[-1] == 'sql':
        df = open(i)
        df = df.read()
        if df.find(first_input) != -1:
            just_massive.append(i)
            cnt += 1

rez_massive = just_massive        
for j in rez_massive:
    print(j)
    
print('Всего: ', cnt)
print('')

while True:
    another_input = input('Введите строку: ')
    just_massive2 = []
    cnt2 = 0
    if another_input == 'exit':
        break
        
    for k in rez_massive:
        df1 = open(k)
        df1 = df1.read()
        if df1.find(another_input) != -1:
            just_massive2.append(k)
            cnt2 += 1
        
    rez_massive = just_massive2    
    for j in rez_massive:
        print(j)
    
    print('Всего: ', cnt2)
    print('')
    if cnt2 = 1:
        break 
    
    cnt2 = 0        

