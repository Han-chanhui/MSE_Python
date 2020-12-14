#!/usr/bin/env python
# coding: utf-8

# In[4]:


리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py'] #주어진 리스트
for i in 리스트:  #리스트의 자료의 개수(4개) 만큼 for문에 종속된 코드를 반복한다.
    split = i.split(".") #리스트 자료를 "."를 기준으로 쪼갠다.(멤버 함수 split() 사용) 
    #쪼개진 자료의 리스트 1번째 값이 "h"이거나 "c"일 경우(둘 중 하나를 만족) 해당 자료를 출력한다.
    if (split[1] == "h") or (split[1] == "c"):
        print(i)

