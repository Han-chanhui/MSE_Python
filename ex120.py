#!/usr/bin/env python
# coding: utf-8

# In[3]:


fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"} #문제에서 정의된 fruit 딕셔너리
user = input("좋아하는 과일은?") #input()함수를 사용하면 데이터를 입력 받을 수 있다.

if user in fruit.values(): #조건문 사용 - 입력값이 딕셔너리의 value에 존재한다면 "정답입니다"를 출력한다.
    print("정답입니다.")
else:                      #입력값이 딕셔너리의 value에 존재하지 않는다면 "오답입니다"를 출력한다. 
    print("오답입니다.")

