// You are building a meeting scheduler for a remote team working across time zones. Each team member provides their available time slots for the day. Your goal is to automatically find the earliest time slot that allows all team members to attend a meeting of a given duration.

// The meeting duration must fit entirely within a time window where all team members are simultaneously available.

// You are not allowed to use any built-in JavaScript functions for time or array manipulation, such as .sort(), .map(), .filter(), .reduce(), Date, or external libraries like moment.js. You must manually calculate and compare time intervals.

// Input:

// 1. teamAvailability: An object where each key is a team member’s name and the value is an array of available time slots. Each time slot is a string in "HH:MM-HH:MM" format, indicating a continuous block of availability in 24-hour time.

// Example:
// teamAvailability = {
// Alice: ["09:00-11:00", "13:00-16:00"],
// Bob:   ["10:00-12:00", "14:00-17:00"],
// Carol: ["08:00-10:30", "15:00-18:00"]
// }

// 2. meetingDuration: A positive integer indicating how many minutes the meeting must last.

// Example:
// meetingDuration = 60

// Output:

// If a valid slot exists where all members are available for the required duration, return an object:
// {
// start: "HH:MM",
// end: "HH:MM"
// }

// If no such slot exists, return:
// "No available slot"

// Expected Output for the above example:
// {
// start: "15:00",
// end: "16:00"
// }

// Explanation:

// All three members are available from 15:00 to 16:00.
// This is the earliest common time window that accommodates a 60-minute meeting.
// Therefore, this time block is selected.

// Test Case 1:

// Input:
// teamAvailability = {
// Alice: [
// "07:00-08:30",
// "09:15-11:00",
// "13:00-14:30",
// "16:00-18:00"
// ],
// Bob: [
// "06:45-08:15",
// "10:30-12:00",
// "13:15-15:00",
// "16:45-17:30"
// ],
// Carol: [
// "08:00-09:00",
// "10:45-11:30",
// "13:00-13:45",
// "17:00-18:00"
// ],
// David: [
// "09:45-11:15",
// "13:30-14:30",
// "16:50-18:00"
// ]
// }

// meetingDuration = 30

// Expected Output:

// {
// start: "17:00",
// end: "17:30"
// }

// Test Case 2:

// Input:
// let teamAvailability = {
// Alice: ["09:00-09:30"],
// Bob: ["09:15-09:45"],
// Carol: ["09:10-09:35"]
// }
// meetingDuration = 15

// Expected Output:
// {
// start: "09:15",
// end: "09:30"
// }

// Test Case 3:

// Input:
let teamAvailability = {
Alice: ["08:00-09:00"],
Bob: ["10:00-11:00"],
Carol: ["12:00-13:00"]
}
meetingDuration = 30

// Expected Output:
// "No available slot"\

//start time : 4:00 22/07/25
//end time  : 11:10 23/07/25

// let teamAvailability = {
// Alice: ["08:00-09:00"],
// Bob: ["08:00-08:30"],
// Carol: ["08:00-13:00"]
// }

// let meetingDuration = 30;

console.log(scheduleMeeting(teamAvailability, meetingDuration))

function scheduleMeeting(teamAvailability, meetingDuration) {
    let meetDurationRange = getmeetDurationRange(teamAvailability, meetingDuration)
    if (meetDurationRange === 0) {
        return "No available slot"
    }
    // console.log(meetDurationRange)
    return {
        "start": meetDurationRange[0].start,
        "end": meetDurationRange[0].end
    }
}

function getmeetDurationRange(teamAvailability, meetingDuration) {
    let personAvailableslots = {} //to check the slots which can actually hold the meeting 
    for (let person in teamAvailability) {
        let slots = isSlotAvailable(teamAvailability[person], meetingDuration);
        if (slots) {
            if (!personAvailableslots[person]) {
                personAvailableslots[person] = slots
            }
        }
    }
    // console.log(personAvailableslots)
    if (Object.keys(teamAvailability).length != Object.keys(personAvailableslots).length) {
        return "No Available Slot"
    }

    let personSlotsData = Object.entries(personAvailableslots)
    let [firstPersonName, firstPersonSlots] = personSlotsData.shift();
    let currentOverlap = []

    for (let i = 0; i < firstPersonSlots.length; i++) {
        let slot1 = firstPersonSlots[i]
        let start1 = slot1.substring(0, slot1.indexOf("-"))
        let end1 = slot1.substring(slot1.indexOf("-") + 1)
        let startMin1 = timeToMinutes(start1)
        let endMin1 = timeToMinutes(end1)

        let valid = true;

        for (let j = 0; j < personSlotsData.length; j++) { //iterating person name and their fretimeslot range 
            let person2Slots = personSlotsData[j][1] //[j]-> ['bob',["07:00-8:30","09:00-10:30"]] ,,[j][1]-> ["07:00-8:30","09:00-10:30"]
            let found = false

            for (let k = 0; k < person2Slots.length; k++) { //iterating the slot of person 
                let slot2 = person2Slots[k]
                let start2 = slot2.substring(0, slot2.indexOf("-"))
                let end2 = slot2.substring(slot2.indexOf("-") + 1)
                let startMin2 = timeToMinutes(start2)
                let endMin2 = timeToMinutes(end2)

                let overlapStart = getMax(startMin1, startMin2) //whichever slot starts last
                let overlapEnd = getMin(endMin1, endMin2) //whichever slot ends first

                if (overlapEnd - overlapStart >= meetingDuration) {
                    startMin1 = overlapStart //setting the new time slot tothe most recent free slot
                    endMin1 = overlapEnd 
                    found = true
                    break //no need to check for another timeslot of same person if we had already found the available timeslot of that person check for next person
                }
            }

            if (!found) { //if we had not found any matching time slot then check next timeslot of first person
                valid = false //we had not found the matching timeslot
                break
            }
        }

        if (valid) { //if the timeslots are overlapping then
            let start = minutesToTime(startMin1)
            let end = minutesToTime(startMin1 + meetingDuration) //end time meeting will be based on meeting duration because endtime can be more thn the actual meeting time 
            currentOverlap.push({ start: start, end: end })
            // console.log(currentOverlap)
            break
        }
    }

    if (currentOverlap.length === 0) {
        return 0
    }

    return currentOverlap
}

function isSlotAvailable(ranges, meetDurationRange) { //get available slots of person from the all free range
    let availableSlotArray = []
    for (let i = 0; i < ranges.length; i++) {
        let slot = ranges[i];
        let slotinMin = getMinInSlot(slot);
        if (isEnoughTime(slotinMin, meetDurationRange)) {
            availableSlotArray.push(slot)
        }
    }
    return availableSlotArray
}

function getMinInSlot(slot) { //get how many minutes are in the slot 
    let startTimeStr = slot.substring(0, slot.indexOf("-"));
    let endTimeStr = slot.substring(slot.indexOf("-") + 1, slot.length)

    let startHour = parseInt(startTimeStr.substring(0, 2))
    let startMin = parseInt(startTimeStr.substring(3, 5))
    let endHour = parseInt(endTimeStr.substring(0, 2))
    let endMin = parseInt(endTimeStr.substring(3, 5))

    return (endHour * 60 + endMin) - (startHour * 60 + startMin)
}

function timeToMinutes(timeStr) { //"07:00"->420
    let hour = parseInt(timeStr.substring(0, 2))
    let min = parseInt(timeStr.substring(3, 5))
    return hour * 60 + min
}

function minutesToTime(totalMinutes) { //420->"7:00"
    let hour = Math.floor(totalMinutes / 60)
    let min = totalMinutes % 60
    let hh = hour < 10 ? "0" + hour : "" + hour  //add zero if the hour is lesser than 10 like "07"/"08" if not then directly add thehour like "12"/"11"
    let mm = min < 10 ? "0" + min : "" + min    //same like hour
    return hh + ":" + mm
}

function isEnoughTime(slotinMin, meetDurationRange) {
    return slotinMin >= meetDurationRange ? 1 : 0;
}

function getMax(val1,val2){
    if(val1>val2){
        return val1
    }else if(val2>val1){
        return val2
    }else{
        return val1
    }
}

function getMin(val1,val2){
    if(val1<val2){
        return val1
    }else if(val2<val1){
        return val2
    }else{
        return val1
    }
}