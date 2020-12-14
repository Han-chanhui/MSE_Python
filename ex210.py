#!/usr/bin/env python
# coding: utf-8

# In[1]:


def message1(): #함수명:message1
    print("A") #함수 내용: "A"를 출력한다. 

def message2(): #함수명:message2
    print("B") #함수 내용: "B"를 출력한다.

def message3(): #함수명:message3
    for i in range (3): #for문에 종속된 코드를 3번 반복실행한다. 
        message2() #message2 함수를 실행한다.(for문 종속)
        print("C") #"C"를 출력한다.(for문 종속)
    message1() #message1 함수를 실행한다. (이 코드는 for문에 종속되어 있지 않다.)

# 따라서, message3()은 for문에 종속된 코드 3번 반복  -> message1() 한번 실행과 같다. 
message3()

