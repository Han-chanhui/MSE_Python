#!/usr/bin/env python
# coding: utf-8

# In[2]:


#주어진 코드 (비트코인의 가격정보를 딕셔너리로 가져오는 코드)
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

#문제에서 지정된 key name에 따라 변동폭, 시가, 최고가를 실수 형태(float)로 지정한다.
변동폭 = float(btc['max_price']) - float(btc['min_price']) #변동폭 = 최고가 - 최저가
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가: #만약 (시가+변동폭)이 최고가보다 클 경우 "상승장"을 출력한다.
    print("상승장") 
else:                      #(시가+변동폭)이 최고가보다 작을 경우 "하락장"을 출력한다.  
    print("하락장")

