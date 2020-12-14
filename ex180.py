#!/usr/bin/env python
# coding: utf-8

# In[5]:


#주어진 리스트
low_prices  = [100, 200, 400, 800, 1000] #저가
high_prices = [150, 300, 430, 880, 1000] #고가

volatility = [] #리스트 이름 설정
#멤버함수 len()을 이용해 low_prices 리스트 자료의 개수를 구하고, 그 개수를 for문의 범위로 설정한다(range).
for i in range(len(low_prices)):
    #고가에서 저가를 뺀 값을 멤버함수 append()를 사용하여 리스트에 추가한다.
    volatility.append(high_prices[i] - low_prices[i]) 
    
print(volatility) #print() 함수를 이용해 리스트를 출력한다. 

