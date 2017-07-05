# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#소스코드를 작성하는 장소

print('Hello world!')
print('Welcome')
print('Hello world!',end=' ')   #붙여나오게 하고 싶을때
print('Welcome')
print('Hello world!',end='t')   #t를 붙이면   
print('Welcome')
print('Hello world!',end='\t')  #\를 붙이면 중간에 공간이 생김
print('Welcome')

#print를 이용해서 6월달 달력 만들기

print('\t\t\t6월')
print('Sun\tMon\tTue\tWed\tThr\tFri\tSat')
print('\t\t\t\t1\t2\t3')                    #반복
print('4\t5\t6\t7\t8\t9\t10')               #반복
print('11\t12\t13\t14\t15\t16\t17')         #반복
print('18\t19\t20\t21\t22\t23\t24')         #반복
print('25\t26\t27\t28\t29\t30')             #반복(1씩증가하는 규칙을 가지므로 반복이다.)

#(주석)을 사용하면 명령을 수행하지않고 지나감.
#우리가 만든 소스코드는 정당한 작업지시이지만, 2017년 6월달에 한정해서 사용밖에....
#한가지 경우에만 적용가능한 코딩을 하드코딩이라고 한다. 
#프로그램의 피해야하는 대원칙
#1)고정된 것을 없애야한다.(하드코딩제거) 2)반복을 제거

#반복을 제거해야한다. -> 반복문
#python이라는 언어는 proto type을 테스트하는 곳에 많이 쓰인다. 
#작업순서 : 의미있는 데이터의 변화 / 프로그램 = 데이터 + 절차
#statement 생성 = 데이터와 연산자의 결합
#같다 ==, : 내밑에 딸린 코드가 있다.

print('\t\t\t10월')
print('Sun\tMon\tTue\tWed\tThr\tFri\tSat')
for i in range(1,32):
    print('%d\t'%i,end='')  #1~31까지 자동으로는 나온다 한줄로 쭉간다, 8을밑으로
    if i==7:
        print()             #분기를 해야한다. 7-8로 넘어갈때 -> if문 사용!
    if i==14:
        print()
    if i==21:
        print()
    if i==28:
        print()
print()

print('\t\t\t10월')
print('Sun\tMon\tTue\tWed\tThr\tFri\tSat')
for i in range(1,32):
    print('%d\t'%i,end='') 
    if i%7==0:
        print() 

print()
print('\t\t\t6월')  #1일이 목요일부터 시작
print('Sun\tMon\tTue\tWed\tThr\tFri\tSat')
print('\t\t\t\t',end='')
for i in range(1,31):
    print('%d\t'%i,end='') 
    if i%7==3:
        print() 
print()

print('\t\t\t6월')  #1일이 목요일부터 시작
print('Sun\tMon\tTue\tWed\tThr\tFri\tSat')
print('\t\t\t\t',end='')
for i in range(1,31):
    print('%d\t'%i,end='') 
    if (i+4)%7==0:
        print() 
print()

space = 6
month = 7
lastDay = 31
print('\t\t\t2017년 %d월'%month)  
print('Sun\tMon\tTue\tWed\tThr\tFri\tSat')
for i in range(space):
    print('\t',end='')
for i in range(1,lastDay+1):
    print('%d\t'%i,end='') 
    if (i+space)%7==0:
        print() 
print()

space = 1
month = 5
lastDay = 31
print('\t\t\t2017년 %d월'%month)  
print('Sun\tMon\tTue\tWed\tThr\tFri\tSat')
for i in range(space):
    print('\t',end='')
for i in range(1,lastDay+1):
    print('%d\t'%i,end='') 
    if (i+space)%7==0:
        print() 
        
print()

space = 1
month = 5
lastDay = 31
print('\t\t\t2017년 %d월'%month)  
print('Sun\tMon\tTue\tWed\tThr\tFri\tSat')
for i in range(space):
    print('\t',end='')
for i in range(lastDay):
    print('%d\t'%(i+1),end='') 
    if (i+1+space)%7==0:
        print() 
#코드를 보고 설명할 수 있어야 한다.
"""
산술 연산자
+,-,*,/,//,%
대입(할당)연산자
=
관계(조건)연산자 (if문에서만)
==,!>,>,>=,<,<=
논리연산자(boolean)
true, false
"""
print()

space = 1
month = 5
lastDay = 31
print('\t\t\t2017년 %d월'%month)  
print('Sun\tMon\tTue\tWed\tThr\tFri\tSat')
print('\t'*space,end='')
for i in range(lastDay):
    print('%d\t'%(i+1),end='') 
    if (i+1+space)%7==0:
        print() 


print()

space = 1
month = 5
lastDay = 31
print('\t\t\t2017년 %d월'%month)  
print('Sun\tMon\tTue\tWed\tThr\tFri\tSat')
for i in range(space):
    print('\t',end='')
for i in range(lastDay):
    print('%d\t'%(i+1),end='') 
    if (i+1+space)%7==0:
        print() 


