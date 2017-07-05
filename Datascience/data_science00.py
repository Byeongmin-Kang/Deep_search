# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 23:24:46 2017

@author: USER
"""

#2.1.3 들여쓰기
for i in [1,2,3,4,5]:
    print(i)
    for j in [1,2,3,4,5]:
        print(j)
        print(i+j)
    print(i)
print("done looping")

long_winded_computation = (1+2+3+4+5+6+7+8+9+10+
                           11+12+13+14+15+16+17+18+19+20)
print(long_winded_computation)

list_of_lists =[[1,2,3],[4,5,6],[7,8,9]]
easier_to_read_list_of_lists = [[1,2,3],
                                [4,5,6],
                                [7,8,9]]
two_plus_three = 2 + \
                 3
print(two_plus_three)
"""
python은 들여쓰기를 통해서 가독성을 높였지만, 코드형태에서 주의 필요
역슬래쉬(\)를 사용하면 코드가 다음줄로 이어지는 것을 명시가능
"""

#2.1.4 모듈
import re
my_regex = re.compile("[0-9]+",re.I)
print(my_regex)

import re as regex
my_regex = regex.compile("[0-9]+",re.I)

import matplotlib.pyplot as plt

from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()
"""
모듈을 불러오기위해서는 import와 .를 사용하면 된다
반복이나 특정하게 부르기 위해서는 as를사용하면된다
"""

#2.1.5 연산
"""
python은 기본적으로 정수 연산이므로 소수를 사용하기 위해서는 특별하게 선언
"""

#2.1.6 함수
def double(x):
    """이 곳은 함수에 대한 설명을 적어 놓는 공간이다. 
    예를들어, "이 함수는 입력된 변수에 2를 곱한 값을 출력해 준다"
    라는 설명을 추가할 수 있다."""
    return x*2
def apply_to_one(f):
    """인자가 1인 함수 f를 호출"""
    return(1)
my_double = double
x = apply_to_one(my_double)
print(x)
y = apply_to_one(lambda x: x+4)
print(y)

def my_print(message="my default message"):
    print(message)
my_print("hello")
my_print()

def subtract(a=0, b=0):
    return a-b
print(subtract(10,5))
print(subtract(0,5))
print(subtract(b=5))
"""
함수란, 0개 혹은 그 이상의 인자를 입력 받아 결과를 출력하는 규칙이다.
"""

#2.1.7 문자열
single_quoted_string = 'data science'
double_quoted_string = "data science"

tab_string = "\t"
len(tab_string) #1

not_tab_string = r"\t"
len(not_tab_string) #2

multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""
"""
문자열(string)은 작은 따옴표 또는 큰 따옴표로 묶어 나타낸다. 
다만, 앞 뒤로 동일한 기호를 사용해야 한다.
"""






