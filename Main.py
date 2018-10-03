
# coding: utf-8

# In[1]:


import os

path = os.path.join(os.getcwd(), 'Migrations')
print(path)
os.chdir(path)
dir_work = os.listdir(path)
a = len(dir_work)
print(a)  


# In[5]:


intermediate = []
rezult = []
cnt = 0
first_input = input('Введите строку: ')
for i in dir_work:
    check = i.split('.')
    if check[-1] == 'sql':
        df = open(i)
        df = df.read()
        if df.find(first_input) != -1:
            intermediate.append(i)
            cnt += 1

rezult = intermediate        
for i in rezult:
    print(i)
    
print('Всего: ', cnt)
print('')

while True:
    another_input = input('Введите строку: ')
    intermediate = []
    cnt = 0
    if another_input == 'exit':
        break
        
    for i in rezult:
        df = open(i)
        df = df.read()
        if df.find(another_input) != -1:
            intermediate.append(i)
            cnt += 1
        
    rezult = intermediate    
    for i in rezult:
        print(i)
    
    print('Всего: ', cnt)
    print('')
    if cnt == 1:
        break 
    
    cnt = 0        

