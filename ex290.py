#!/usr/bin/env python
# coding: utf-8

# In[2]:


class 부모: #부모 클래스 설정
  def __init__(self): #함수 설정
    print("부모생성")

class 자식(부모): #자식 클래스 설정
  def __init__(self): #함수 설정
    print("자식생성")
    super().__init__() #super 키워드를 통해 '부모 class'에 접근할 수 있다. 이를 통해 "부모생성"의 생성자를 호출한다.  

#코드 실행
나 = 자식()

