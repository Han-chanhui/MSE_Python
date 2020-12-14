#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random

#은행 계좌 생성
class Account:
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []

        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        # 3-2-6 계좌번호 생성
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  
        num2 = str(num2).zfill(2)  
        num3 = str(num3).zfill(6)  
        self.account_number = num1 + '-' + num2 + '-' + num3  
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count

    def deposit(self, amount): #입금시 입금 내역을 저장하는 코드
        if amount >= 1:
            self.deposit_log.append(amount)
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                # 이자 지금
                self.balance = (self.balance * 1.01)


    def withdraw(self, amount): #출금시 출금 내역을 저장하는 코드
        if self.balance > amount:
            self.withdraw_log.append(amount)
            self.balance -= amount
    
    def display_info(self): #정보 출력
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    def withdraw_history(self): #출금 내역 저장
        for amount in self.withdraw_log:
            print(amount)

    def deposit_history(self): #입금 내역 저장
        for amount in self.deposit_log:
            print(amount)


k = Account("Kim", 1000)
k.deposit(100) #100원 입금
k.deposit(200) #200원 입금
k.deposit(300) #300원 입금
k.deposit_history() #deposit_history 함수 호출

k.withdraw(100) #100원 출금
k.withdraw(200) #200원 출금
k.withdraw_history() #withdraw_history 함수 호출


# In[ ]:




