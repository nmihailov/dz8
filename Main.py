
# coding: utf-8

# In[ ]:


import os

path = os.getcwd() + '\Migrations'
print(path)
os.chdir(path)
dir_work = os.listdir(path)
a = len(dir_work)

search = input('Введите искомое слово:')
result = []
for i in range (0, a):
    if dir_work[i].find(search) != -1:
        result.append(dir_work[i])
        print(dir_work[i])

print('----------------------------------------------')
print('')
b = len(result)
while True:
    search2 = input('Введите искомое слово точнее:')
    for i in range(0, b):
        if result[i].find(search2) != -1:
            print(result[i])
        

