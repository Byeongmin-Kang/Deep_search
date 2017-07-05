# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 16:30:21 2017

@author: user
"""

#professor's 핵심 coding
import random
word = "internationalization"
length = int(len(word)*0.2)
print(length)
position_index = []
for i in range(length):
    position_index.append(random.randrange(len(word)))

print(position_index)
for i in range(len(word)):
    if i in position_index:
        print('_',end='')
    else :
        print(word[i],end='')

"""
print(position_index)
for i in range(len(word)):
    if i == position_index[0] or i == position_index[1] :
        print('_',end='')
    else :
        print(word[i],end='')
"""    

letter = input('please input letter >> ')
for i in position_index:
    if letter == word[i]:
        print('존재')
    else :
        print('없음')
        
temp_list = [1,2,1,3]
temp_list.remove(1) #value
print(temp_list)
del temp_list #index
print(temp_list)
