#!/usr/bin/env python
# coding: utf-8

# In[9]:


def print_max(a, b, c): #3개의 수 (a,b,c)에 대한 함수 print_max를 정의한다.
    #함수 내용: 조건문과 비교 연산자를 사용하여 a가 b와 c보다 크면 a를 출력한다. 
    if a > b and a > c:
        print(a)
    #함수 내용: 조건문과 비교 연산자를 사용하여 b가 a와 c보다 크면 b를 출력한다.
    elif b > c and b > a:
        print(b)
     #함수 내용: 위의 경우를 제외했을 때, 즉 c가 a와 b보다 크면 c를 출력한다.
    else:
        print(c)
    
#함수 출력의 예시는 다음과 같다. 
print_max(12, 34, 5)

