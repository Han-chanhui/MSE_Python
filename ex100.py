#!/usr/bin/env python
# coding: utf-8

# In[2]:


#주어진 2개의 리스트
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

#함수 zip() 은 같은 개수로 이루어진 자료형을 하나로 묶어주는 기능을 한다.
#zip()으로 묶은 데이터를 dic()을 통해 딕셔너리 형태로 변환한다.  
close_table = dict(zip(date, close_price))
print(close_table) #print 함수를 이용해 출력한다. 

