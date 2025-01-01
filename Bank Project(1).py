#!/usr/bin/env python
# coding: utf-8

# # Name: Muhammad Huzaifa 
# # ID No: AI-333873
# 
# ## Bank Project

# In[1]:


def accountopening():
    account={}
    print("ENTER YOUR NAME:")
    account["Name"]=input().capitalize()
    account["Balance"]=0
    account["Transactions"]=[]
    print(f"Account for {account["Name"]} created with balance {account["Balance"]}$.")
    return account

def deposit():
    try:
        amount=0
        print("Enter A Number To Deposit")
        inp=float(input())

        if inp<0:
            print("Enter A Value Greater Than 0")
            return 0
        else:
            amount=inp
            return amount
    except:
        pass
        

def withdraw():
    try:
        ammount=0
        print("Enter A Number To Withdraw")
        inp=float(input())
        if inp<0:
            print("Enter A Value Greater Than 0")
            return 0
        else:
            ammount=inp
            return ammount
    except:
        pass


# In[2]:


data=0
if_running=True
print("Welcome to Huzaifa Bank Pvt. Ltd.")
while if_running:
    print("Please Selecet (1) To Open An Account And Then Select A Choice From (2-6)\n1.Account Opening\n2.Check Balance\n3.Deposit Ammount\n4.Withdraw Ammount\n5.Account Statment\n6.Exit")
    try:
        num=int(input())
    except:
        print("Enter A Number")
    if num==1:
        data=accountopening()
    elif num==2:
        print(f"Current balance is {data["Balance"]}$.")
    elif num==3:
        try:
            ammount=deposit()
            data["Balance"]+=ammount
            print(f"{data["Name"]} deposited {ammount}$.New balance is now {data["Balance"]}$.")
            data["Transactions"].append(ammount)
        except:
            print("Please Enter A Number")
    elif num==4:
        try:
            ammount=withdraw()
            if ammount>data["Balance"]: 
                print("Insufficient Balance")
            else:
                data["Balance"]-=ammount
                print(f"{data["Name"]} withdrew {ammount}$.New balance is now {data["Balance"]}$.")
                data["Transactions"].append(-ammount)
        except:
            print("Please Enter A Number")    
    elif num==5:
        blnc=0
        print(f"Account Statement of {data["Name"]}")
        for a in data["Transactions"]:
            if a >0:
                blnc+=a
                print(f"--Deposited: {a}$. New Balance: {blnc}$.")
            elif a<0:
                blnc+=a
                print(f"--Withdrawal: {-a}$. New Balance: {blnc}$.")
    elif num ==6:
        if_running=False    
        print("Thank You For Using Our Services")
    else:
        print("Please Enter A Valid Choice")
        
        


# In[ ]:





# In[ ]:




