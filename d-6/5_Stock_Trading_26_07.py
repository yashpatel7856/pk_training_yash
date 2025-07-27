# Problem 3: Real-Time Stock Trading Simulator with Order Book and Matching Engine

# Problem Statement

# Simulate a real-time stock trading platform with order matching logic and portfolio tracking. The system should:

# Accept Buy and Sell limit orders.
# Match orders based on price-time priority using an order book.
# Allow partial fills.
# Update user portfolios and balances upon trades.
# Log executed trades.


# Sample Input

# python
# user1 = User("Alice", 10000)
# user2 = User("Bob", 5000)
# stock = Stock("TSLA", 800)

# book = OrderBook()
# book.add_order(Order(user1, stock, 5, 810, "BUY"))
# book.add_order(Order(user2, stock, 5, 800, "SELL"))

# book.match_orders()
# print(user1.portfolio)
# print(user2.balance)

# Sample Output

# Trade: 5 shares of TSLA at 800
# {'TSLA': 5}
# 9000

# start time : 6:05
# end time : 

class User:
    def __init__(self,name,walletBalance):
        self.name=name
        self.walletBalance=walletBalance
        self.portfolio={}
class Stock:
    def __init__(self,name,basePrice,stockQuantity):
        self.name=name
        self.stockQuantity=stockQuantity
        self.basePrice=basePrice
        self.availableInMarket=stockQuantity

class Order:  #Order(user1, stock, 5, 810, "BUY")
    def __init__(self,user,stock,stockQuantity,stockPrice,orderType):
        self.user=user
        self.stock=stock
        self.stockQuantity=stockQuantity
        self.stockPrice=stockPrice
        self.orderType=orderType

class OrderBook:
    def __init__(self):
        self.order_book=[]

    def add_Order(self,order) :
        self.order_book.append(order.__dict__)

    def match_orders(self):
        pass
        sellOrders={}
        buyOrders={}
        for order in self.order_book:  
            if order["stock"].availableInMarket>=order["stockQuantity"]:
                if order["orderType"]=='BUY':
                    buyOrders[order["stock"].name]=order["stockQuantity"]
                else:
                    sellOrders[order["stock"].name]=order["stockQuantity"]
            else:
                print(f'Can not {order["orderType"]} stocks more than the quantity available in market order discarded')
        print("sellOrder---",sellOrders)
        print("buyOrder----",buyOrders)



user1 = User("Alice", 10000)
user2 = User("Bob", 5000)
stock = Stock("TSLA", 800,555)

book = OrderBook()
book.add_Order(Order(user1, stock, 5, 810, "BUY"))
book.add_Order(Order(user2, stock, 5, 800, "SELL"))

book.match_orders()
# print(user1.portfolio)
# print(user2.balance) 