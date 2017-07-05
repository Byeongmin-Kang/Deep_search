# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 13:04:49 2017

@author: user
"""
#데이터를 분할해보기
data = [
        '990001addx 17 29 16 49 43154CAC',
        '990002stch 30  9 48 25 81193CAA',
        '990003gali 93 60  6 84 36297ACA',
        '990004miat 73 22 48 24 72239BCC',
        '990005oran 33 38 59 58 28216CBA',
        ]

print(len(data)) #결과 4

#step2 ->분할
inner_list = []
for i in range(len(data)):
    inner_list.append(data[i][:6])
    inner_list.append(data[i][6:10])
    inner_list.append(data[i][11:13])
    inner_list.append(data[i][14:16])
    inner_list.append(data[i][17:19])
    inner_list.append(data[i][20:22])
    inner_list.append(data[i][23:25])    
    inner_list.append(data[i][25:28])    
    inner_list.append(data[i][28:29]) 
    inner_list.append(data[i][29:30]) 
    inner_list.append(data[i][30:31]) 
print(inner_list)

#step3 -> out_list에 저장
outer_list = []
for i in range(len(data)):
    inner_list = []
    inner_list.append(data[i][:6])
    inner_list.append(data[i][6:10])
    inner_list.append(data[i][11:13])
    inner_list.append(data[i][14:16])
    inner_list.append(data[i][17:19])
    inner_list.append(data[i][20:22])
    inner_list.append(data[i][23:25])    
    inner_list.append(data[i][25:28])    
    inner_list.append(data[i][28:29]) 
    inner_list.append(data[i][29:30]) 
    inner_list.append(data[i][30:31]) 
    outer_list.append(inner_list)
print(len(outer_list[0]))
print(outer_list)
print(outer_list[0])

#step4 총점 구하기
sum = 0
for i in range(len(outer_list)):
    sum = sum + int(outer_list[i][7])
print(sum)

#step5 평균구하기
print('반 전체 총점평균은 = %f'%(sum/len(outer_list))) #%6.2f를 붙이면 소수점 2자리까지

