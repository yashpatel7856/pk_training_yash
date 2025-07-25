# // You are building a meeting scheduler for a remote team working across time zones. Each team member provides their available time slots for the day. Your goal is to automatically find the earliest time slot that allows all team members to attend a meeting of a given duration.

# // The meeting duration must fit entirely within a time window where all team members are simultaneously available.

# // You are not allowed to use any built-in JavaScript functions for time or array manipulation, such as .sort(), .map(), .filter(), .reduce(), Date, or external libraries like moment.js. You must manually calculate and compare time intervals.

# // Input:

# // 1. teamAvailability: An object where each key is a team member’s name and the value is an array of available time slots. Each time slot is a string in "HH:MM-HH:MM" format, indicating a continuous block of availability in 24-hour time.

# // Example:
# // teamAvailability = {
# // Alice: ["09:00-11:00", "13:00-16:00"],
# // Bob:   ["10:00-12:00", "14:00-17:00"],
# // Carol: ["08:00-10:30", "15:00-18:00"]
# // }

# // 2. meetingDuration: A positive integer indicating how many minutes the meeting must last.

# // Example:
# // meetingDuration = 60

# // Output:

# // If a valid slot exists where all members are available for the required duration, return an object:
# // {
# // start: "HH:MM",
# // end: "HH:MM"
# // }

# // If no such slot exists, return:
# // "No available slot"

# // Expected Output for the above example:
# // {
# // start: "15:00",
# // end: "16:00"
# // }

# // Explanation:

# // All three members are available from 15:00 to 16:00.
# // This is the earliest common time window that accommodates a 60-minute meeting.
# // Therefore, this time block is selected.

# // Test Case 1:

# // Input:
# // teamAvailability = {
# // Alice: [
# // "07:00-08:30",
# // "09:15-11:00",
# // "13:00-14:30",
# // "16:00-18:00"
# // ],
# // Bob: [
# // "06:45-08:15",
# // "10:30-12:00",
# // "13:15-15:00",
# // "16:45-17:30"
# // ],
# // Carol: [
# // "08:00-09:00",
# // "10:45-11:30",
# // "13:00-13:45",
# // "17:00-18:00"
# // ],
# // David: [
# // "09:45-11:15",
# // "13:30-14:30",
# // "16:50-18:00"
# // ]
# // }

# // meetingDuration = 30

# // Expected Output:

# // {
# // start: "17:00",
# // end: "17:30"
# // }

# // Test Case 2:

# // Input:
# // let teamAvailability = {
# // Alice: ["09:00-09:30"],
# // Bob: ["09:15-09:45"],
# // Carol: ["09:10-09:35"]
# // }
# // meetingDuration = 15

# // Expected Output:
# // {
# // start: "09:15",
# // end: "09:30"
# // }

# // Test Case 3:

# // Input:
# let teamAvailability = {
# Alice: ["08:00-09:00"],
# Bob: ["10:00-11:00"],
# Carol: ["12:00-13:00"]
# }
# meetingDuration = 30

# // Expected Output:
# // "No available slot"\

# //start time : 1:00
# //end time  : 3:50

import copy

teamAvailability = {
 "Alice": ["08:00-09:00","09:00-10:30"],
 "Bob": ["08:01-08:10","09:28-09:42"],
 "Carol": ["08:00-13:00"]
 }

meetingDuration = 5



def getMinInSlot(slot):
    startTimeStr=slot[0:slot.index('-')]
    endTimeStr=slot[slot.index('-')+1:]
    startHour=int(startTimeStr[:2])
    startMin=int(startTimeStr[3:5])
    endHour=int(endTimeStr[:2])
    endMin=int(endTimeStr[3:5])
    print((endHour * 60 + endMin) - (startHour * 60 + startMin))
    return (endHour * 60 + endMin) - (startHour * 60 + startMin)

def timeToMinute(str1):
    hour=int(str1[:2])
    min=int(str1[3:5])
    return (hour*60) + min

def minutesToTime(minutes):
    hour=int(minutes/60)
    min=minutes%60
    if hour<10:hh="0"+str(hour)
    else:hh=""+str(hour)
    if min<10:mm="0"+str(min)
    else:mm=""+str(min)
    return hh+":"+mm

def isEnoughTime(slotInMin,meetingDuration):
    if slotInMin>=meetingDuration:return 1
    else:return 0

def getMax(v1,v2):
    if v1>v2:
        return v1
    elif v2>v1:
        return v2
    else:
        return v1

def getMin(v1,v2):
    if v1<v2:
        return v1
    elif v2<v1:
        return v2
    else:
        return v1

def getPersonAvailability(teamAvailability,meetingDuration):
    ""
    for person in teamAvailability:
        for slot in teamAvailability[person]:
                if getMinInSlot(slot)<meetingDuration:
                    print(slot)
                    teamAvailability[person].pop(teamAvailability[person].index(slot))
        print(person)
    print(teamAvailability)
    tempKeyList=list(teamAvailability.keys()) # if we use dic_keys list then it will be auto updated and then it would have given error.
    delKeyList=[]
    try:
        for person in tempKeyList:
            if len(teamAvailability[person])==0:
                del teamAvailability[person]
                # delKeyList.append(person)
        # for person in delKeyList:
        #     del teamAvailability[person]
    except:
        print("error of delting the object key")
    return teamAvailability

def scheduleMeeting(teamAvailability,meetingDuration):
    ""
    overLapData={}
    personAvailability=getPersonAvailability(copy.deepcopy(teamAvailability),meetingDuration)
    if len(personAvailability.keys()) != len(teamAvailability.keys()):
        return "No Slot Available"
    
    personSlotData=list(personAvailability.items())

    firstPersonSlots=personSlotData[0][1]
    personSlotData.pop(0)

    for slot in firstPersonSlots:
        start1=slot[0:slot.index('-')]
        end1=slot[slot.index('-')+1:]
        startMin1=timeToMinute(start1)
        endMin1=timeToMinute(end1)

        valid=True

        for personData in personSlotData:
            found=False
            for person2Slot in personData[1]:
                start2=person2Slot[0:person2Slot.index('-')]
                end2=person2Slot[person2Slot.index('-')+1:]
                startMin2=timeToMinute(start2)
                endMin2=timeToMinute(end2)
                
                overlapStart=getMax(startMin1,startMin2)
                overlapEnd=getMin(endMin1,endMin2)

                if overlapEnd-overlapStart >= meetingDuration:
                    startMin1=overlapStart
                    endMin1=overlapEnd
                    found=True
                    break
            if not found:
                valid=False
                break
        if valid:
            start=minutesToTime(startMin1)
            end=minutesToTime(startMin1+meetingDuration)
            overLapData["start"]=start
            overLapData["end"]=end
            break
    if not overLapData.get("start"):
        return "No slots Available"
    return overLapData


print(scheduleMeeting(teamAvailability,meetingDuration))


