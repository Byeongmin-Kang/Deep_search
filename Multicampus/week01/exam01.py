# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 16:41:59 2017

@author: user
"""

print(1+2)
sum = 1+2   #저장하는 완결O #Fixed
print(sum)  #출력 완결O 

sum = 2+3   #sum의 값은 변경되지만, 안의 숫자는 고정되어있다!!!!!!!!
print('sum = ',sum)

print(1+2)
num1 = 2
num2 = 4
sum = num1 + num2       #식은 고정 
print('sum = ',sum)     #그러나 값이 변경된다. 데이터의 변수화~~~!!!!
print(1+2+3+4+5)        #고정.....
print((1+2+3+4+5)/5)    #평균 but, 원하지 않은 결과..... #중복....
total = 1+2+3+4+5
print(total)            #변수에 데이터를 저장하고, 가져와서 사용!! 고정과 중복의 회피가 가능!
print(total/5)          #중복을 제거 (변수에 넣어라) 변수가 매우 중요하다는 것!!!!!!
print(1+2+3+4+5/5)      #연산자의 우선순위를 반드시 고려해야한다.!!!!!
print('1-2 = ',1-2)
print('3/5 = ',3/5)
print('3//5 = ',3//5)
print('7/5 = ',7/5)
print('7//5 = ',7//5)   # //은 몫이다!!!
print('4%5 = ',4%5)     # %나머지!


#숫자를 분리하는 프로그램을 만들어보자!
#나머지 연산자를 잘 활용해야한다!!!!!!!!
number = 123456
print(number%10)
print(number%100//10)
print(number%1000//100)
print(number%10000//1000)
print(number%100000//10000)
print(number%1000000//100000)
print(number%1000000//100000)
print(number%100000//10000)
print(number%10000//1000)
print(number%1000//100)
print(number%100//10)
print(number%10)

#그냥 숫자의 자리수를 하나씩 줄여가는 것으로 가능하다.
number = number//10
print(number%10)
#이렇게 반복하면됩니다. 이렇게하면 중복이 생기는데 중복제거 -> 반복문사용

#자리수가 6자리로 고정되어 있다.
#-> 개선점!!!!, 자리수를 자동으로 감지하는 것이 필요
#몇번반복해야할지 모를 때, while 반복문을 사용하면 됩니당~

number = 123456
sum = 0
for i in range(6):
    temp = number%10
    sum = sum + temp
    print(temp)
    number = number//10

print('sum => ', sum) 

#무한 반복 -> While 반복이 확정되면 while문을 쓸 필요없어용 그래서 아래의 형태가 맞음
#어떤 조건이 되면 break해라!!

while True:
    if      :
        break -> 반복문을 빠져나갈 때 사용하는 키워드 

number = 123456
while True:
    temp = number%10
    print(temp)
    number = number//10
    if number == 0:
        break

number = 1234
while True:
    temp = number%10
    print(temp)
    number = number//10
    if number == 0:
        break

#개수에 관계없이 처리가능하다!!!!!!!!!!

number = 123456
sum = 0
while True :
    temp = number%10
    sum = sum + temp
    number =number//10
    if number == 0 :
        break
print('sum = ',sum)

