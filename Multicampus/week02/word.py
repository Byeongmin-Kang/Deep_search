# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 17:06:16 2017

@author: user

    만약에 word_l의 원소를 다 검사하는데, 
    이 원소중에 'p'와 일치하는 성분이 있다면,
    p를 '_'로 바꿔라


1. 단어 10개는 주어진다. (complete)

2. 단어를 출력하는 함수 (사용자에게 단어하나를 출력) 
(만들어야함)
3. 출력된 단어에서, 단어의 20%를 선택하는 함수
4. 선택된 알파벳을 변환하는 함수  
# changeword
5. 사용자가 입력한 알파벳을 비교하는 함수
6. 

1-5반복 
언제든지 나갈수 있도록 break

"""
wordlist = ['coffee','apply','pocket','google','water','programming','disappointed','neighbor','pronunciation','dangerous']
import random
import word_module
#print(len(wordlist[1]))
for i in range(len(wordlist)):
    if len(wordlist[i])<8 :
        delete_word = random.choice(wordlist[i])
        word_p = word_module.shortchangeword(wordlist[i],delete_word)
        print(word_p)
        while True :
            in_word = input('단어를 입력해주세요 -> ') 
            
            if delete_word == in_word:
                print('%s정답입니다. 다음 문제로 갈게요'%wordlist[i])
                break
            else :
                print('다시 입력해주세요.')
    else :
        delete_word1 = random.choice(wordlist[i])
        delete_word2 = random.choice(wordlist[i])
        if delete_word1==delete_word2:
                    delete_word2 = random.choice(wordlist[i])
        word_p = word_module.longchangeword(wordlist[i],delete_word1,delete_word2)
        print(word_p)
        while True :
            in_word1 = input('단어를 입력해주세요 -> ')
            if delete_word1 == in_word1 : 
                word_p = word_module.shortchangeword(wordlist[i],delete_word2)
                print('%s오~ 하나 맞추셨어용.!! 하나더!! -> '%word_p)
                in_word2 = input('하나 더 입력해주세요 -> ')
                if delete_word1 == in_word2 or delete_word2 == in_word2 :
                    print('%s 맞추셨어요!! 다음문제~'%wordlist[i])
                    break
            elif delete_word2 == in_word1:
                word_p = word_module.shortchangeword(wordlist[i],delete_word1)
                print('%s오~ 하나 맞추셨어용.!! 하나더!! -> '%word_p)
                in_word2 = input('하나 더 입력해주세요 -> ')
                if delete_word1 == in_word2 or delete_word2 == in_word2:
                    print('%s 맞추셨어요!! 다음문제~'%wordlist[i])
                    break
            else :
                print('다시 입력해주세요.')
        
        
