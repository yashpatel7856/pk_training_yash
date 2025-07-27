# Problem 1: Realistic Event Booking System with Wallet, Pricing Strategy, and Seat Types

# Problem Statement

# Design a robust event booking system that handles multiple seat types, user membership tiers, wallet balances, and flexible pricing strategies. The system must support:

# Multiple seat categories (VIP, General, Balcony) with limited capacities.
# Pricing based on seat type and user tier (Regular, Gold, Platinum).
# Booking confirmation with real-time seat deduction and wallet charge.
# Cancellation with 80% refund and seat restoration.
# Custom pricing logic via the Strategy Pattern.


# Sample Input

# python
# event = Event("Comedy Night", 500, {"VIP": 5, "General": 10, "Balcony": 8})
# user = User("Amit", "Gold", 5000)

# booking = Booking(user, event, "VIP", 2, DefaultPricing())
# booking.confirm()   # Booking seats
# booking.cancel()    # Cancel and refund

#  Sample Output

# Amit booked 2 VIP seat(s) for Comedy Night at 1800.0
# Booking canceled. Amit refunded 1440.0

# start time : 3:03
# end time : 4:06

class Event:
    def __init__(self,eventName,minSeatingPrice,seatingCapacity):
        self.eventName=eventName
        self.minSeatingPrice=minSeatingPrice
        self.seatingCapacity=seatingCapacity

class User:
    def __init__(self,userName,userTier,walletBalance):
        self.userName=userName
        self.userTier=userTier
        self.walletBalance=walletBalance

class Bookings:
    isBooked=False
    bookingCost=0
    def __init__(self,user,event,seatType,quantity,pricingStrategy):
        self.user=user
        self.event=event
        self.seatType=seatType
        self.quantity=quantity
        self.pricingStrategy=pricingStrategy
        
    def confirm(self):
        ticketCost=self.pricingStrategy.calculatePrice(self.seatType,self.quantity,self.user.userTier,self.event.minSeatingPrice) #seatType,seatQuantity,membershipType,eventBasePrice
        if(self.user.walletBalance>=ticketCost):
            if(self.event.seatingCapacity[self.seatType]>=self.quantity): ## can add more checks (user try to booking more than the total seats then available seat number can be given to user )
                Bookings.isBooked=True
                Bookings.bookingCost=ticketCost
                self.event.seatingCapacity[self.seatType]-=self.quantity
                self.user.walletBalance-=ticketCost
                print(f"{self.user.userName} Booked {self.quantity} {self.seatType} Seat(s) for {self.event.eventName} at {ticketCost}")
                return f"{self.user.userName} Booked {self.quantity} {self.seatType} Seat(s) for {self.event.eventName} at {ticketCost}"
            else:
                print("Selected Seats are already booked try different block")
                return "Selected Seats are already booked try different block"
        else:
            print("Insufficient User Balance" )
            return "Insufficient User Balance"   

    def cancel(self):
        if Bookings.isBooked:
            refundAmount=Bookings.bookingCost*0.80
            self.user.walletBalance+=refundAmount
            print(f"Your Booking is Canceled Successfully.{refundAmount} will be deposited to your wallet")
            return f"Your Booking is Canceled Successfully.{refundAmount} will be deposited to your wallet"
        else:
            print("Your Booking is Not Confirmed Yet.Please Confirm Your Booking First !!!")
            return "Your Booking is Not Confirmed Yet.Please Confirm Your Booking !!!!"

class DefaultPricing:
    seatPricing={
        "VIP":2,
        "General":1.5,
        "Balcony":1
    }
    memberShipDiscount={  #Regular, Gold, Platinum
        "Regular":0,
        "Gold":10,
        "Platinum":20
    }
    def calculatePrice(self,seatType,seatQuantity,membershipType,eventBasePrice):
        seatPrice=DefaultPricing.seatPricing[seatType] * eventBasePrice * seatQuantity
        customerDiscount=seatPrice * (DefaultPricing.memberShipDiscount[membershipType]/100)
        actualBookingPrice=seatPrice-customerDiscount
        return actualBookingPrice

event = Event("Comedy Night", 500, {"VIP": 4, "General": 10, "Balcony": 8})
user = User("Amit", "Gold", 6800)

booking = Bookings(user, event, "VIP", 2, DefaultPricing())
booking.confirm()   # Booking seats
booking.cancel()    # Cancel and refund