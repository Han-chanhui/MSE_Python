#!/usr/bin/env python
# coding: utf-8

# In[2]:


리스트 = ["가", "나", "다", "라"] #주어진 리스트
#리스트 slicing(자르기)를 이용한다. 슬라이싱은 리스트[시작인덱스:종료인덱스:변화의 폭]으로 지정한다.
#따라서, 리스트[::-1] (처음부터 끝까지 -1만큼씩 증가)로 입력하면 원하는 결과를 얻을 수 있다. 
for a in 리스트[::-1]:
    print(a) #print()함수로 출력한다. 
