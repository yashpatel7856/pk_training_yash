# 2. Dynamic Library Fine Calculator

# Problem Statement:

# Create a library fine calculator where the late return fine varies by day type:

# * Weekdays: ₹2/day for first 5 days, ₹5/day after that
# * Weekends: Fine is doubled
# * More than 10 days late adds ₹20 flat penalty
# * Premium members receive a 40% discount

# Sample Input:

# ```
# Late days: 12  
# Days: [Mon, Tue, Wed, Thu, Fri, Sat, Sun, Mon, Tue, Wed, Thu, Fri]  
# Membership: Premium
# ```

# Sample Output:

# ```
# Total fine before discount: ₹116  
# Final fine: ₹69.6
# ```

# start time : 10:55
# end time : 11:20


fine= {
    "Late_days": 12 ,
    "Days": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"],
    "Membership": "Premium"
}

def calculateFine(fine):
    dayCount = 0
    totalFine = 0
    multiplier=1
    baseFine=getWeekDayFine()["base"]
    for day in fine["Days"]:
        dayCount+=1
        if dayCount>5:
            baseFine=getWeekDayFine()["late"]
        if day=="Sat" or day=="Sun":
            multiplier=2
            totalFine+= baseFine * multiplier
            multiplier=1
        else:
            totalFine+=baseFine * multiplier

    # 10 days flat fine
    if dayCount>10:
                totalFine+=20

    print(f'total fine before discount{totalFine}')
    if fine["Membership"]== "Premium":
        totalFine=totalFine-totalFine*0.4
    print(f'total fine after discount { totalFine}')
    return totalFine
            

def getWeekDayFine():
    return {
        "base" : 2,
        "late" : 5
    }

print(calculateFine(fine))