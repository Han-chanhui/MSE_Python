#!/usr/bin/env python
# coding: utf-8

# In[2]:


if True: #조건1 - 참일 경우 (조건1은 참이므로 True에 종속된 코드가 실행된다.)
    if False: #조건2 - 참일 경우 (조건2는 거짓이므로 이 코드는 실행되지 않는다.)
        print("1")
        print("2")
    else: #조건2 - 거짓일 경우 (조건2는 거짓이므로 이 코드가 실행된다.)
        print("3")
else: #조건1 - 거짓일 경우 (조건1은 참이므로 else에 종속된 코드는 실행되지 않는다.)
    print("4")

#print("5")는 앞에서 나온 조건문에 종속되지 않으므로 조건문과 상관없이 출력된다.
print("5")

