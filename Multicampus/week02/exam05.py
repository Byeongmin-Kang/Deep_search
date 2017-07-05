# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 13:09:58 2017

@author: user
"""

#step6 함수 만들기
#data set = 정보를 가지고 있는 리스트 = outer_list
def get_average(dataset,index): #index -> 우리가 원하는 과목 
    sum = 0
    for i in range(len(dataset)): #data set의 행의 수 만큼 반복
        sum = sum + int(dataset[i][index])
        
    return sum/len(dataset)

#step7
import mymodule
subject = ['Eng','Math','Geo','Stat','Leter']
average = mymodule.get_average(outer_list,6)

print('%s 평균은 = %6.2f'%(subject[6-2],average))

#step8 추가 함수만들기
def make_dataset(raw_data):
    outer_list = []
    for i in range(len(raw_data)):
        inner_list = []
        inner_list.append(raw_data[i][:6])
        inner_list.append(raw_data[i][6:10])
        inner_list.append(raw_data[i][11:13])
        inner_list.append(raw_data[i][14:16])
        inner_list.append(raw_data[i][17:19])
        inner_list.append(raw_data[i][20:22])
        inner_list.append(raw_data[i][23:25])    
        inner_list.append(raw_data[i][25:28])    
        inner_list.append(raw_data[i][28:29]) 
        inner_list.append(raw_data[i][29:30]) 
        inner_list.append(raw_data[i][30:31]) 
        outer_list.append(inner_list)
    return outer_list

#step9 새로운 함수 사용해보기
import mymodule
mymodule.make_dataset(data)