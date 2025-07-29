# Problem 6: Cash Register System
# Create a simple cash register system to manage client information and balances.
# Requirements:
# You can add new users with their name and phone number.

# You can view a user's details, including their current balance.

# You must be able to add to or deduct from a user's balance.

# The balance cannot go negative.

# You can search for a user by username or phone number.

# Use a JSON file to store all user data persistently.

# Record the date and time of the last transaction for each user.

# Transaction Requirements:
# Maintain a transaction history for each user.

# Provide an option to:

# Display all past transactions.

# Show the total spending so far.

# Show the details of the highest and lowest spending bills.

# If a transaction is made on a weekend, apply a 30% discount automatically.

# Allow applying a discount code "OFF30%" to apply a 30% discount on the transaction (can be used any day).

# Apply 18% GST to every transaction after applying any discounts.

# Notes:
# Discounts should be applied before calculating GST.

# Keep the system simple and focused on core logic and file handling.
 
# Documentation Requirement:
# Before starting the implementation:
# Create a brief documentation that explains:
# Your core logic and reasoning behind your approach.
# How you plan to structure the code (e.g., using functions or classes).
# How you will handle:
# File operations (reading/writing JSON),
# Balance updates and validations,
# Discounts and GST calculations,
# Transaction history tracking.

# start time : 3:00
# end time :   3:37 29/07/2025

import time
import json
import os
import sys

class User:
    def __init__(self,name,userName,mobileNumber,walletBalance):
        pass
        self.name=name
        self.userName=userName
        self.mobileNumber=mobileNumber
        self.walletBalance=walletBalance
        self.transactions=[]
        self.lowestTransactionValue=0
        self.highestTransactionValue=0
        self.recentPurchaseTimeStamp=None

    def updateUserTransactions(self,transaction):
        self.walletBalance-=transaction.purchaseAmount
        self.transactions.append({"purchaseAmount":transaction.purchaseAmount,"timestamp":transaction.timestamp})
        print(self.transactions)
        self.recentPurchaseTimeStamp=time.time()
        if transaction.purchaseAmount<self.lowestTransactionValue or self.lowestTransactionValue==0:
            self.lowestTransactionValue=transaction.purchaseAmount
        if transaction.purchaseAmount>self.highestTransactionValue:
            self.highestTransactionValue=transaction.purchaseAmount

    def getPurchaseHistory(self):
        return self.transactions

    def getWalletBalance(self):
        return self.walletBalance
    
    def isPurchaseable(self,purchaseAmount):
        if purchaseAmount<=self.walletBalance:
            return True
        else:
            return False
        
    @staticmethod
    def createNewUser(name,userName,phoneNumber):
        user =User(name,userName,phoneNumber,sys.maxsize)
        return user.__dict__

    @staticmethod
    def updateUserData(transaction):
        defaultFileName='user_data.json'
        userdata=None
        
        if not os.path.exists(defaultFileName):
            with open(defaultFileName,'w') as f:
                transaction.user["walletBalance"]-=transaction.purchaseAmount
                transaction.user["lowestTransactionValue"]=transaction.purchaseAmount
                transaction.user["highestTransactionValue"]=transaction.purchaseAmount
                transaction.user["recentPurchaseTimeStamp"]=transaction.timestamp
                transaction.user["transactions"].append({"purchaseAmount":transaction.purchaseAmount,"timestamp":transaction.timestamp})
                f.write(json.dumps([transaction.user]))
                return

        with open(defaultFileName,"r+") as file:
            try:
                userdata=json.load(file)
            except json.JSONDecodeError:
                userdata=[] # just in case reading fails program will not crash only the data will be lost
            tempUserObj=None
            flag=False
            tempUserList=[]
            for user in userdata: 
                if user["mobileNumber"]==transaction.user["mobileNumber"]:
                    if user["walletBalance"]<transaction.purchaseAmount:
                        print(f'Insufficient Funds user={user["name"]},Balance={user["walletBalance"]}')
                        return 0
                    user["walletBalance"]-=transaction.purchaseAmount
                    user["transactions"].append({"purchaseAmount":transaction.purchaseAmount,"timestamp":transaction.timestamp})
                    if user["lowestTransactionValue"] >transaction.purchaseAmount or  user["lowestTransactionValue"]==0: 
                        user["lowestTransactionValue"] = transaction.purchaseAmount
                    if user["highestTransactionValue"] < transaction.purchaseAmount:
                        user["highestTransactionValue"]=transaction.purchaseAmount
                    user["recentPurchaseTimeStamp"]=transaction.timestamp
                    flag=False
                    break
                else:
                    tempUserObj=transaction.user
                    flag=True
            if flag:
                tempUserObj["walletBalance"]-=transaction.purchaseAmount
                if tempUserObj["lowestTransactionValue"]> transaction.purchaseAmount or tempUserObj["lowestTransactionValue"]==0:
                    tempUserObj["lowestTransactionValue"]=transaction.purchaseAmount
                if tempUserObj["highestTransactionValue"]<transaction.purchaseAmount:
                    tempUserObj["highestTransactionValue"]=transaction.purchaseAmount
                tempUserObj["transactions"].append({"purchaseAmount":transaction.purchaseAmount,"timestamp":transaction.timestamp})
                tempUserObj["recentPurchaseTimeStamp"]=transaction.timestamp
                tempUserList.append(tempUserObj)
            userdata+=tempUserList
            file.seek(0)  ## move the pointer to strt of file
            file.truncate() ##delete all data of file
            json.dump(userdata, file)
            
            # json.dump(userdata,file)
            
#  defaultFileName='user_data.json'
#         userData=None
#         with open(defaultFileName,'r+') as file:
#             userData=json.load(file)
#         for user in userData:
#             if user["mobileNumber"]==data or user["userName"]==data:
#                 print(user)
#                 return user
      

class Transaction:
    def __init__(self,user,purchaseAmount,timestamp=time.time()):
        # self.user=user.__dict__
        self.purchaseAmount=purchaseAmount
        self.timestamp = timestamp
        if isinstance(user, User):
            self.user=user.__dict__
        else:
            self.user=user

class CashRegister:
    customerOfTheMonth=None
    def __init__(self,shopName):
        self.shopName=shopName
        self.transactionHistory=[]
    
    def checkOut(self,user,purchaseAmount,coupon=''):
        weekDay=time.localtime().tm_wday
        month=time.localtime().tm_mon
        discount=0

        if CashRegister.customerOfTheMonth!=None:
            if CashRegister.customerOfTheMonth["month"] == month and CashRegister.customerOfTheMonth["mobileNumber"]==user["mobileNumber"]:
                discount+=0.1

        if weekDay>=5:
            discount=0.3 #30%
        
        if coupon=="OFF30%":
            discount+=0.3
        
        beforeTaxValue=purchaseAmount-purchaseAmount*discount
        finalInvoiceValue=beforeTaxValue+beforeTaxValue*0.18

        transaction=Transaction(user,finalInvoiceValue)
        User.updateUserData(transaction)
        self.transactionHistory.append(transaction.__dict__)
        return transaction

    def getTransactionHistory(self):
        return self.transactionHistory
    
    @staticmethod
    def getTotalBillingAmount():
        nextItem=True
        totalAmount=0
        while nextItem:
            iteName=input("enter item Name")
            itemPrice=input("enter item Price")
            totalAmount+=int(itemPrice)
            nextItem=input("is there any next item ?(1/0)")
            if nextItem=="0":
                break   
        return totalAmount

    def saveUserData(self,*userArgs):
        defaultFileName='user_data.json'
        userList=[]
        for u in userArgs:
            userList.append((u.__dict__))
        with open(defaultFileName,"w") as file :
            json.dump(userList,file)
    
    def findUserData(self,data):
        defaultFileName='user_data.json'
        userData=None
        with open(defaultFileName,'r') as file:
            try:
                userData=json.load(file)
            except json.JSONDecodeErro:
                userData=[]
        for user in userData:
            if user["mobileNumber"]==data or user["userName"]==data:
                print(user)
                totalspendings=0
                for transaction in user["transactions"]:
                    totalspendings+=transaction["purchaseAmount"]
                print(f'current total Spending = {totalspendings}  ')
                return user
        print("No user Found with this phone number")
        return 0

    @staticmethod
    def GetCustomerOfTheMonth():
        currentMonth=time.localtime(time.time()).tm_mon
        userDataObj={
            "mobileNumber":"",
            "monthTotalTransactionAmount":0
        }##data of user who have transaction in current month
        defaultFileName='user_data.json'
        userData=None
        with open(defaultFileName,'r') as file:
            try:
                userData=json.load(file)
            except json.JSONDecodeErro:
                userData=[]
        for user in userData:
            totalTransactionAmount=0
            hasCurrentMonthTransactions=False
            for transaction in user["transactions"]:
                if currentMonth==time.localtime(transaction["timestamp"]).tm_mon:
                    totalTransactionAmount+=transaction["purchaseAmount"]
                    hasCurrentMonthTransactions=True
            if hasCurrentMonthTransactions:
                if userDataObj["monthTotalTransactionAmount"]<totalTransactionAmount:
                    userDataObj["monthTotalTransactionAmount"]=totalTransactionAmount
                    userDataObj["mobileNumber"]=user["mobileNumber"]
                    userDataObj["name"]=user["name"]
        if userDataObj["monthTotalTransactionAmount"]!=0:
            CashRegister.customerOfTheMonth={
                                                "monthTotalTransactionAmount":userDataObj["monthTotalTransactionAmount"],
                                                "mobileNumber":userDataObj["mobileNumber"],
                                                "month":currentMonth
                                            }
            print(f'{userDataObj["name"]} is customer of the month[{currentMonth}]. total spendings={userDataObj["monthTotalTransactionAmount"]}')
            return 
        print("No customer chhosen to be customer of the month")
        


        


# u1=User("yash","yashpatel7856","9510877350",100000)
# u2=User("raj","raj080","5123456789",100)

c1=CashRegister("hariom veg")


def startRegister():
        nextBill=True
        getCustomerOfTheMonth=int(input("do you want to get customer of the month  yes=1 ,no=0"))
        if getCustomerOfTheMonth==1:
            CashRegister.GetCustomerOfTheMonth()
        getUserData=int(input("to find a user data enter 1"))
        if getUserData==1:
            phoneNumber=input("enter users phone number to find")
            c1.findUserData(phoneNumber)
        while nextBill:

            userId=int(input("To create new user enter 1"))
            if userId==1:
                user=User.createNewUser(*getUserDatafromUser())
            else:
                phoneNumber=input("enter phone number of existing customer")
                if len(phoneNumber)!=10:
                    print("enter valid 10 digit phone number")
                    continue
                user=c1.findUserData(phoneNumber)
                if user==0:
                    continue

            purchaseAmount=CashRegister.getTotalBillingAmount()
            coupon=input("enter coupon code if any")
            transaction=c1.checkOut(user,purchaseAmount,coupon)

            nextBill=input("stop billing / close shop(0/1)")
            if nextBill=="0":
                break

            

def getUserDatafromUser():
    name=input("enter User Name")
    userName=input("enter a userName ")
    phoneNumber=input("enter user phone number")

    return (name,userName,phoneNumber)

startRegister()