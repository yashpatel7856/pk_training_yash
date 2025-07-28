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
# end time : 10:42

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

    def add_Order(self,order):
        self.order_book.append(order.__dict__)

    def match_orders(self):
        remaining_orders = []

        for buy_order in self.order_book:
            if buy_order["orderType"] != "BUY":
                remaining_orders.append(buy_order)
                continue

            for sell_order in self.order_book:
                if sell_order["orderType"] != "SELL":
                    continue

                if buy_order["stock"].name != sell_order["stock"].name:
                    continue

                if buy_order["stockPrice"] >= sell_order["stockPrice"] and buy_order["stockQuantity"] > 0 and sell_order["stockQuantity"] > 0:
                    traded_qty = min(buy_order["stockQuantity"], sell_order["stockQuantity"])
                    trade_price = sell_order["stockPrice"] #when buyer is willing to pay more price but he can get same thing at cheaper price order book will give him lower price 

                    if buy_order["user"].walletBalance<traded_qty * trade_price:
                        print(f'{buy_order["user"].name} do not have sufficient Funds in Wallet to Complete the trade')
                        continue

                    buy_order["user"].walletBalance -= traded_qty * trade_price
                    sell_order["user"].walletBalance += traded_qty * trade_price

                    if buy_order["stock"].name in buy_order["user"].portfolio:
                        buy_order["user"].portfolio[buy_order["stock"].name] += traded_qty
                    else:
                        buy_order["user"].portfolio[buy_order["stock"].name] = traded_qty

                    if sell_order["stock"].name in sell_order["user"].portfolio:
                        if sell_order["user"].portfolio[sell_order["stock"].name] >= traded_qty:
                            sell_order["user"].portfolio[sell_order["stock"].name]-=traded_qty
                        else:
                            pass ## traded quantity is greater than actual stock quantity in portfolio
                    else:
                        pass ##stock is not present in portfolio

                    buy_order["stockQuantity"] -= traded_qty
                    sell_order["stockQuantity"] -= traded_qty

                    print(f"Trade: {traded_qty} shares of {buy_order['stock'].name} at {trade_price}")
                    break

            if buy_order["stockQuantity"] > 0:
                remaining_orders.append(buy_order)

        self.order_book = [order for order in remaining_orders if order["stockQuantity"] > 0] 
        # print(self.order_book) 

user1 = User("Alice", 10000)
user2 = User("Bob", 5000)
stock = Stock("TSLA", 800, 100)

book = OrderBook()
book.add_Order(Order(user1, stock, 5, 810, "BUY"))
book.add_Order(Order(user2, stock, 10, 800, "SELL"))
book.add_Order(Order(user1, stock, 5, 810, "BUY"))

book.match_orders()

print(user1.portfolio)
print(user1.walletBalance)
print(user2.walletBalance)