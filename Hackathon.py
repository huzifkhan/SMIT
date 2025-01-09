#!/usr/bin/env python
# coding: utf-8

# # Muhammad Huzaifa
# # AI-333873
# 
# ## Hackathon

# In[1]:


class BalanceException(Exception):
    # A class only created for exceptions as defined by name
    pass

class Bank:
    def __init__(self,holdername,holderbalance):
        self.name=holdername
        self.balance=holderbalance
        self.transactions=[]
        print(f"\nAccount Created Sucessfully For {self.name}.")
    def HolderName(self):
        print(f"\nAcccount Registered On The Name of {self.name}.")
    def Balance(self):
        print(f"\nCurrent Balance of {self.name} is Rs.{self.balance}")
    def Deposit(self,amount):
        # To Deposit amount
        self.balance=self.balance+amount
        print("Deposit Successfully...")
        self.Balance()
        self.add_transactions(f"Deposit : {amount}")
    def CheckTransactions(self,amount):
        # This is created to check amount for withdrawl and bank transfer 
        if self.balance>=amount:
            return
        else:
            raise BalanceException(f"\nSorry The Account of {self.name} has balance of Rs.{self.balance}..")
    def Withdraw(self,amount):
        # To Withdraw money from account
        try:
            self.CheckTransactions(amount)
            self.balance=self.balance-amount
            print("\nWithdraw Successfully...")
            self.Balance()
            self.add_transactions(f"Withdraw : {amount}")
        except BalanceException as Error:
            print(f"\nWithdraw Interupted... : {Error}")
    def add_transactions(self,description):
        self.transactions.append(description)

    def print_statement(self):
        for a in self.transactions:
            print(a)
    def BankTransfer(self,amount,account):
        # To transfer amount from one account to another
        try:
            print("\nProcessing...")
            self.CheckTransactions(amount)
            self.Withdraw(amount)
            account.Deposit(amount)
            print("\nCompleted...")
        except BalanceException as error:
            print(f"\nTransfer Interupted... : {error}")
        


# In[2]:


accounts={}


# In[5]:


run=True

while run:
    print("\nWelcome to Hackathon Bank.\nSelect Your Desired Option\n1)Open Account\n2)Check Balance\n3)Deposit Amount\n4)Withdraw Amount\n5)Bank Transfer\n6)Exit\n7)Admin Access")
    try:
        # Ask to see which number would a person choose
        print("\nEnter Your Choice..")
        option=int(input())
    except:
        print("\nEnter An Interger..")

    if option==1:
        print("\nWelcome")
        try:
            print("\nEnter Your Desired Four Digit **** Unique Number..")
            accountnumber=int(input())
            print("\nEnter Your Name..")
            name=input().capitalize()
            print("\nDeposit Starting Amount..")
            firstam=int(input())
            accounts[accountnumber]=Bank(name,firstam)
        except:
            print("\nPlease Follow Instructions..")
    elif option==2:
        print("\nWelcome")
        try:
            print("\nEnter Your Four Digit **** Account Number..")
            accnum=int(input())
            accounts[accnum].Balance()
        except:
            print("\nPlease Follow Instructions..")
    elif option==3:
        print("\nWelcome")
        try:
            print("\nEnter Your Four Digit **** Account Number..")
            accnum=int(input())
            print("\nEnter Amount To Deposit..")
            amount=int(input())
            accounts[accnum].Deposit(amount)
        except:
            print("\nPlease Follow Instructions..")
    elif option==4:
        print("\nWelcome")
        try:
            print("\nEnter Your Four Digit **** Account Number..")
            accnum=int(input())
            print("\nEnter Amount To Deposit..")
            amount=int(input())
            accounts[accnum].Withdraw(amount)
        except:
            print("\nPlease Follow Instructions..")
    elif option==5:
        try:
            print("\nEnter Your Four Digit **** Account Number..")
            accnum=int(input())
            print("\nEnter Benificary Four Digit **** Account Number..")
            baccnum=int(input())
            print("\nEnter Amount To Transfer..")
            amount=int(input())
            accounts[accnum].BankTransfer(amount,accounts[baccnum])
        except:
            print("\nPlease Follow Instructions..")

    elif option==6:
        print("\nThanks For Using Our Services..")
        run=False
    elif option==7:
        print("Default Password For Admin Is 0000..")
        try:
            inp=int(input())
            if inp==0000:
                for a in accounts.values():
                    a.HolderName()
                    a.Balance()
                    a.print_statement()
            else:
                print("Enter Correct Password..")
        except:
            print("Follow Instructions...")

