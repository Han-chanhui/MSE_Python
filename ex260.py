#!/usr/bin/env python
# coding: utf-8

# In[3]:


class OMG: #주어진 클래스 OMG 
    def print(): #함수를 지정한다.
        print("Oh my god") #함수내용: "Oh my god"을 출력
        
myStock = OMG() 
myStock.print() 
#OMG() = myStock이므로 이 코드는 위에 정의된 OMG 클래스를 통해 실행되게 된다. 
#하지만, 두번째 줄의 def print(): 함수에서 print 내용에 해당하는 출력값이 없기 때문에 에러가 발생한다. 


# In[4]:


class OMG :
    def print(mystock) : #따라서, print에 mystock을 지정해주면 해결할 수 있다. 
        print("Oh my god")


mystock = OMG()
mystock.print()

