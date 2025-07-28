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
# end time : 

import time
import json
import os

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
    def updateUserData(transaction):
        defaultFileName='user_data.json'
        userdata=None
        
        if not os.path.exists(defaultFileName):
            with open(defaultFileName,'w+') as f:
                transaction.user["lowestTransactionValue"]=transaction.purchaseAmount
                transaction.user["highestTransactionValue"]=transaction.purchaseAmount
                transaction.user["recentPurchaseTimeStamp"]=transaction.timestamp
                transaction.user["transactions"].append({"purchaseAmount":transaction.purchaseAmount,"timestamp":transaction.timestamp})
                f.write(json.dumps([transaction.user]))
                return

        with open(defaultFileName,"a+") as file:
            userdata=json.load(file)
            for user in userdata:
                if user["mobileNumber"]==transaction.user["mobileNumber"]:
                    user["transactions"].append({"purchaseAmount":transaction.purchaseAmount,"timestamp":transaction.timestamp})
                    if user["lowestTransactionValue"] >transaction.purchaseAmount or  user["lowestTransactionValue"]==0: 
                        user["lowestTransactionValue"] = transaction.purchaseAmount
                    if user["highestTransactionValue"] < transaction.purchaseAmount:
                        user["highestTransactionValue"]=transaction.purchaseAmount
                    user["recentPurchaseTimeStamp"]=transaction.timestamp
            json.dump(userdata,file)
            
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
        self.user=user.__dict__
        self.purchaseAmount=purchaseAmount
        self.timestamp=timestamp

class CashRegister:
    def __init__(self,shopName):
        self.shopName=shopName
        self.transactionHistory=[]
    
    def checkOut(self,user,purchaseAmount,coupon=''):
        weekDay=time.localtime().tm_wday
        discount=0
        if weekDay>=5:
            discount=0.3 #30%
        
        if coupon=="OFF30%":
            discount+=0.3
        
        beforeTaxValue=purchaseAmount-purchaseAmount*discount
        finalInvoiceValue=beforeTaxValue+beforeTaxValue*0.18

        if user.isPurchaseable(finalInvoiceValue):
            transaction=Transaction(user,finalInvoiceValue)
            user.updateUserData(transaction)
            self.transactionHistory.append(transaction.__dict__)
            return transaction
        else:
            print(f"Insufficient Balance. user={user.name}, walletBalance={user.walletBalance}")
            return f"Insufficient Balance. user={user.name}, walletBalance={user.walletBalance}"


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
        with open(defaultFileName,'w+') as file:
            userData=json.load(file)
        for user in userData:
            if user["mobileNumber"]==data or user["userName"]==data:
                print(user)
                return user
        print("No user Found with this phone number")
        return "No User found"


u1=User("yash","yashpatel7856","9510877350",100000)
u2=User("raj","raj080","5123456789",235)

c1=CashRegister("hariom veg")

# c1.checkOut(u1,100,"OFF30%")
# c1.checkOut(u1,100)
# c1.checkOut(u2,199)



# c1.findUserData("preet07")


def startRegister():
        nextBill=True
        while nextBill:
            u1=User("yash","yashpatel7856","9510877350",100000)
            u2=User("raj","raj080","5123456789",235)
            userId=int(input("enter user id(1/2)"))
            if userId==1:
                print("u1")
                user=u1
            else:
                user=u2
            purchaseAmount=CashRegister.getTotalBillingAmount()
            coupon=input("enter coupon code if any")
            transaction=c1.checkOut(user,purchaseAmount,coupon)

            nextBill=input("stop billing / close shop(0/1)")
            if nextBill=="0":
                break

startRegister()