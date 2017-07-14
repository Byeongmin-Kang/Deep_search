# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 14:35:09 2017

@author: user
"""
outer_line = []
file = open('install.csv','r')
lines = file.readlines()
for line in lines:
    outer_line.append(list(line))
    
print(len(outer_line))

counts = [0,0,0,0]
june = []
july = []
for line in range(1,len(outer_line)):
    temp = lines[line][:-1].split(",")
    #print(temp)
    
    if temp[0].split("-")[1] == '04':
        counts[0] = counts[0] + 1
    elif temp[0].split("-")[1] == '05':
        counts[1] = counts[1] + 1
    elif temp[0].split("-")[1] == '06':
        june.append(temp[2])
        counts[2] = counts[2] + 1
    elif temp[0].split("-")[1] == '07':
        july.append(temp[2])
        counts[3] = counts[3] + 1
print(counts)        
#print(len(june))
#print(len(july))  

solve2 = []
file1 = open('dpu-won.csv','r')
m_lines = file1.readlines()
for i in range(1,len(m_lines)): 
    solve2.append(m_lines[i][:-1].split(","))

tot1 = [] #except june
sub1 = [] #june
tot = [] #except july
sub = [] #july
for line in solve2:
    if line[0].split("-")[1]=='07':
        if line[2] in july:
            sub.append(int(line[3]))
        else :    
            tot.append(int(line[3]))
    elif line[0].split("-")[1]=='06':
        if line[2] in june:
            sub1.append(int(line[3]))
        else :    
            tot1.append(int(line[3]))        
        

june_total = 0
june_except_total = 0
july_total = 0
july_except_total = 0
for item in tot:
    july_except_total = july_except_total+item
for item2 in sub:
    july_total = july_total+item2
print('july total is %d'%(july_total+july_except_total))    
print('july except amount = %d, july amount= %d'%(july_except_total,july_total))    
    
for item in tot1:
    june_except_total = june_except_total+item
for item2 in sub1:
    june_total = june_total+item2

print('june total is %d'%(june_total+june_except_total))    
print('june except amount = %d, june amount= %d'%(june_except_total,june_total))    
print('july = %d, june = %d'%(len(sub),len(sub1)))    
      
       
        
        
        