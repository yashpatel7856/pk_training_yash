# Design a smart traffic signal controller that simulates how traffic lights should operate at a 4-way intersection (North, South, East, West). The controller must decide which direction gets the green signal and in what order — based on vehicle types, urgency, and congestion — all within a fixed time slot. The logic must not use any built-in JavaScript functions such as .sort(), .forEach(), Math.max(), etc.

# Rules and Logic:

# 1. Emergency Vehicle Priority:

#    - Directions containing emergency vehicles (ambulance, firetruck, police) must be given top priority.
#    - Among all such directions:

#      - The one with the emergency vehicle having the highest waitTime gets the green signal first.
#      - If multiple emergency vehicles have the same maximum waitTime, break the tie using the fixed direction priority:
#        North > South > East > West

# 2. Congestion-Based Priority (Fallback):
#    If no emergency vehicles are present in any unserved direction, choose the direction with the highest congestion.
#    Congestion is calculated by summing the waitTime of all vehicles in that direction’s queue.

# 3. Green Signal Constraints:

#    - Each direction can receive a green signal only once per cycle.
#    - Once a direction is selected, vehicles in that direction are allowed to pass one by one until either:

#      - The timeSlot runs out, or
#      - All vehicles in that direction are passed

#   Note: timeSlot – A number indicating the total available time (in seconds) to process traffic in the current cycle. Consider a timeSlot of 60 seconds for this simulation.

# 4. Time Taken Per Vehicle Type:

#    - car: 5 seconds
#    - bus: 10 seconds
#    - bike: 3 seconds
#    - ambulance/firetruck/police: 10 seconds

# 5. Cycle Completion Conditions:

#    - The simulation ends when the total time used reaches or exceeds timeSlot,
#      or
#    - All directions have been processed once.

# 6. No Built-In JavaScript Functions:
#    You must implement all logic manually — without using:
#    .sort(), .map(), .reduce(), .forEach(), Math.floor(), Math.max(), .filter(), etc.

# Input:

# 1. traffic – An object containing vehicle queues for each direction. Each queue is an array of vehicle objects with:

#    - type: Type of vehicle — "car", "bus", "bike", "ambulance", "firetruck", or "police"
#    - waitTime: Number representing how long (in seconds) the vehicle has been waiting

#    Example:

#    traffic = {
#   North: [
#     { type: "ambulance", waitTime: 20 },
#     { type: "car", waitTime: 30 }
#   ],
#   South: [
#     { type: "firetruck", waitTime: 20 },
#     { type: "car", waitTime: 25 }
#   ],
#   East: [
#     { type: "car", waitTime: 50 },
#     { type: "bus", waitTime: 20 }
#   ],
#   West: [
#     { type: "car", waitTime: 40 }
#   ]
# };

# timeSlot = 60;

# Example Output:

# {
#   orderOfGreen: ["North", "South", "East"],
#   vehiclesPassed: {
#     North: ["ambulance", "car"],
#     South: ["firetruck", "car"],
#     East: ["car"],
#     West: []
#   },
#   timeUsed: 60,
#   directionsSkipped: ["West"]
# }

# Explanation of Example:

# Both North and South have emergency vehicles with the same waitTime = 20
# The tie is resolved by direction order → North > South
# North is served first due to the updated rule
# Then South
# Then East by congestion
# West is skipped

# start time : 10:20
# end time : 12:53

traffic = {
  "North": [
    { "type": "ambulance", "waitTime": 20 },
    { "type": "car", "waitTime": 30 }
  ],
  "South": [
    { "type": "firetruck", "waitTime": 30 },
    { "type": "car", "waitTime": 25 },
  ],
  "East": [
    { "type": "firetruck", "waitTime": 50 },
    { "type": "car", "waitTime": 50 },
    { "type": "bus", "waitTime": 20 },
    { "type": "car", "waitTime": 50 },
    { "type": "bus", "waitTime": 20 },
    { "type": "car", "waitTime": 50 },
    { "type": "car", "waitTime": 20 },
  ],
  "West": [
    { "type": "bus", "waitTime": 500 },
    { "type": "bus", "waitTime": 20 },
    { "type": "bus", "waitTime": 50 },
    { "type": "bus", "waitTime": 20 },
    { "type": "car", "waitTime": 50 },
    { "type": "car", "waitTime": 20 }
    ]
}
timeSlot=55




def startSignal(trafiic,timeSlot):
    "main function working"
    # print("inside startsignal")
    greenSignalDirection,vehicalPassed,remainingTime,remainingTraffic,skippedDirections=passEmergencyVehicals(trafiic,timeSlot)
    greenSignalDirection,vehicalPassed,remainingTime,skippedDirection=passCommonVehical(greenSignalDirection,vehicalPassed,remainingTime,remainingTraffic,skippedDirections)
    return{
        "orderOfGreen":greenSignalDirection,
        "vehicalPassed":vehicalPassed,
        "timeUsed":timeSlot-remainingTime,
        "directionsSkipped":skippedDirection
    }

def passEmergencyVehicals(traffic,timeSlot):
    ""
    greenSignalOrder=[]
    vehicalPassed={}
    skippedDirections=[]
    # print("passing emergency vehicals")
    emergencyVehicals,newtraffic=getEmergencyVehicalsFromTraffic(traffic)
    for vehical in emergencyVehicals:
        if timeSlot > 0:
            if(timeSlot>=getVehicalPassingTime(vehical.get("type"))):
                timeSlot-=getVehicalPassingTime(vehical.get("type"))
                if vehical.get("direction") not in vehicalPassed:
                    vehicalPassed[vehical.get("direction")]=[]
                    vehicalPassed[vehical.get("direction")].append(vehical.get('type'))
                else:
                    vehicalPassed[vehical.get("direction")].append(vehical.get('type'))
                greenSignalOrder.append(vehical.get("direction"))
            else:
                if vehical['direction'] not in skippedDirections:
                    skippedDirections.append(vehical['direction'])
        else:
            if vehical['direction'] not in skippedDirections:
                skippedDirections.append(vehical['direction'])
            break
    return(greenSignalOrder,vehicalPassed,timeSlot,newtraffic,skippedDirections)


def getEmergencyVehicalsFromTraffic(traffic):
    newTraffic={}
    emergencyVehicalList=[]
    for direction in traffic:
        for vehical in traffic[direction]:
            if vehical.get("type") in getEmergencyVehicals():
                emergencyVehicalList.append({**vehical,"direction":direction})
            else:
                if direction not in newTraffic:
                    newTraffic[direction]=[]
                    newTraffic[direction].append(vehical)
                else:
                    newTraffic[direction].append(vehical)
    sortedEmergencyVehicals=getTimeSortedEmgVehicals(emergencyVehicalList)
    # print(sortedEmergencyVehicals)
    return sortedEmergencyVehicals,newTraffic

def getTimeSortedEmgVehicals(emergencyVehicalList):
    emergencyVehicalList=sorted(emergencyVehicalList,key=lambda emgVehical:emgVehical["waitTime"],reverse=True)
    # code to sort vehicals based on their direction if have same direction
    return emergencyVehicalList

def getVehicalPassingTime(vehicalType):
    if vehicalType=="car":return 5
    elif vehicalType=="bus":return 10
    elif vehicalType=="bike":return 3
    elif vehicalType=="ambulance":return 10
    elif vehicalType=="firetruck":return 10
    elif vehicalType=="police":return 10
    else:return 0

def passCommonVehical(greenSignalDirection,vehicalPassed,remainingTime,remainingTraffic,skippeddirections):
    "passing common vehicals"
    vehicalCongetion=getVehicalCongetion(remainingTraffic,vehicalPassed)
    # print(vehicalCongetion)

    for direction in vehicalCongetion:
        if remainingTime>0:
            for vehical in vehicalCongetion[direction]['vehicals']:
                if(remainingTime>=getVehicalPassingTime(vehical)):
                    remainingTime-=getVehicalPassingTime(vehical)
                    if direction not in vehicalPassed:
                        vehicalPassed[direction]=[vehical]
                        greenSignalDirection.append(direction)
                    else:
                        vehicalPassed[direction].append(vehical)
                else:
                    if direction not in vehicalPassed:
                        skippeddirections.append(direction)
                    break
        else:
            if direction not in vehicalPassed:
                skippeddirections.append(direction)
            break
    return greenSignalDirection,vehicalPassed,remainingTime,skippeddirections


def getVehicalCongetion(traffic,vehicalPassed):
    vehicalCongetion={}
    sum=0
    for key in vehicalPassed:
        if key in traffic:
            del traffic[key]
    # print(traffic)
    for direction in traffic:
        if direction not in vehicalCongetion:
            # vehicalCongetion[direction]={"vehicals":[vehical["type"] for vehical in traffic[direction]],"totalWaitTime":[sum+=vehical["waitTime"] for vehical in traffic[direction] ]}
            vehicalCongetion[direction]={"vehicals":[vehical["type"] for vehical in traffic[direction]],"totalWaitTime":getVehicalCongetionTotal(traffic[direction])}
    
    # emergencyVehicalList=sorted(emergencyVehicalList,key=lambda emgVehical:emgVehical["waitTime"],reverse=True)
    # vehicalCongetion=dict(sorted(student_scores.items(), key=lambda item: item[1]))
    vehicalCongetion=dict(sorted(vehicalCongetion.items(),key=lambda item:item[1]["totalWaitTime"],reverse=True))
    # print(vehicalCongetion)
    return vehicalCongetion

def getVehicalCongetionTotal(vehicalList):
    totalWaitTime=0
    for vehical in vehicalList:
        totalWaitTime+=vehical['waitTime']
    return totalWaitTime   

def defaultDirection():
    return ("north","South", "East", "West")

def getEmergencyVehicals():
    return ("ambulance","firetruck","police")




print(startSignal(traffic,timeSlot))