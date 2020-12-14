#!/usr/bin/env python
# coding: utf-8

# In[3]:


result = 1 #첫번째 결과값을 1로 설정한다. 
for i in range(1,11): #for문이 돌아갈 횟수를 설정한다(1부터 10까지): range(시작, 끝 - 1)
    #첫번째 result를 1로 설정. 계산해서 나온 결과를 다시 result로 놓고 for문을 돌린다. 
    #for 문이 돌아가는 횟수만큼 계속해서 계산한다. 
    result = result * i
print(result) #print() 함수를 사용해서 출력한다. 

