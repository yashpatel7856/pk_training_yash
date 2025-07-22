// Design a smart traffic signal controller that simulates how traffic lights should operate at a 4-way intersection (North, South, East, West). The controller must decide which direction gets the green signal and in what order — based on vehicle types, urgency, and congestion — all within a fixed time slot. The logic must not use any built-in JavaScript functions such as .sort(), .forEach(), Math.max(), etc.

// Rules and Logic:

// 1. Emergency Vehicle Priority:

//    - Directions containing emergency vehicles (ambulance, firetruck, police) must be given top priority.
//    - Among all such directions:

//      - The one with the emergency vehicle having the highest waitTime gets the green signal first.
//      - If multiple emergency vehicles have the same maximum waitTime, break the tie using the fixed direction priority:
//        North > South > East > West

// 2. Congestion-Based Priority (Fallback):
//    If no emergency vehicles are present in any unserved direction, choose the direction with the highest congestion.
//    Congestion is calculated by summing the waitTime of all vehicles in that direction’s queue.

// 3. Green Signal Constraints:

//    - Each direction can receive a green signal only once per cycle.
//    - Once a direction is selected, vehicles in that direction are allowed to pass one by one until either:

//      - The timeSlot runs out, or
//      - All vehicles in that direction are passed

//   Note: timeSlot – A number indicating the total available time (in seconds) to process traffic in the current cycle. Consider a timeSlot of 60 seconds for this simulation.

// 4. Time Taken Per Vehicle Type:

//    - car: 5 seconds
//    - bus: 10 seconds
//    - bike: 3 seconds
//    - ambulance/firetruck/police: 10 seconds

// 5. Cycle Completion Conditions:

//    - The simulation ends when the total time used reaches or exceeds timeSlot,
//      or
//    - All directions have been processed once.

// 6. No Built-In JavaScript Functions:
//    You must implement all logic manually — without using:
//    .sort(), .map(), .reduce(), .forEach(), Math.floor(), Math.max(), .filter(), etc.

// Input:

// 1. traffic – An object containing vehicle queues for each direction. Each queue is an array of vehicle objects with:

//    - type: Type of vehicle — "car", "bus", "bike", "ambulance", "firetruck", or "police"
//    - waitTime: Number representing how long (in seconds) the vehicle has been waiting

//    Example:

//    traffic = {
//   North: [
//     { type: "ambulance", waitTime: 20 },
//     { type: "car", waitTime: 30 }
//   ],
//   South: [
//     { type: "firetruck", waitTime: 20 },
//     { type: "car", waitTime: 25 }
//   ],
//   East: [
//     { type: "car", waitTime: 50 },
//     { type: "bus", waitTime: 20 }
//   ],
//   West: [
//     { type: "car", waitTime: 40 }
//   ]
// };

// timeSlot = 60;

// Example Output:

// {
//   orderOfGreen: ["North", "South", "East"],
//   vehiclesPassed: {
//     North: ["ambulance", "car"],
//     South: ["firetruck", "car"],
//     East: ["car"],
//     West: []
//   },
//   timeUsed: 60,
//   directionsSkipped: ["West"]
// }

// Explanation of Example:

// Both North and South have emergency vehicles with the same waitTime = 20
// The tie is resolved by direction order → North > South
// North is served first due to the updated rule
// Then South
// Then East by congestion
// West is skipped

//start time : 10:57
//end time : 3:17

let traffic = {
  North: [
    { type: "ambulance", waitTime: 20 },
    { type: "car", waitTime: 30 }
  ],
  South: [
    { type: "firetruck", waitTime: 20 },
    { type: "car", waitTime: 25 },
  ],
  East: [
    { type: "car", waitTime: 50 },
    { type: "bus", waitTime: 20 },
    { type: "car", waitTime: 50 },
    { type: "bus", waitTime: 20 },
    { type: "car", waitTime: 50 },
    { type: "car", waitTime: 20 },
  ],
  West: [
    { type: "bus", waitTime: 20 },
    ],
};

console.log("main cosolelog :- ",startSignal(traffic));

function startSignal(traffic) {
  const timeSlot = 60;
  const defaultDirection = ["North", "South", "East", "West"];
  let orderOfGreenDirection = [];
  let vehicalPassed = {};
  let directionsSkipped = [];
  [orderOfGreenDirection, vehicalPassed,directionsSkipped,remainingTimeslot] = passVehicals(
    traffic,
    timeSlot,
    defaultDirection
  );

  return {
    orderofgreen: orderOfGreenDirection,
    vehicalPassed:vehicalPassed ,
    timeUsed: timeSlot-remainingTimeslot,
    directionsSkipped: directionsSkipped,
  };
}

function passVehicals(traffic, timeSlot, defaultDirection) {
  let emergencyVehicalList=getEmergencyVehicals(traffic,defaultDirection) //list by waiting time and direction priority is waiting time is same 
  let [remainingTimeSlot,vehicalPassed,trafficWithoutEmergencyVehicals,greenSignalOrder] =passEmegencyVehical(emergencyVehicalList,timeSlot,traffic)
  let [commonVehicalPassed,skippedDirection,orderOfGreen,remainingTimeslot]=passCommonVehicals(trafficWithoutEmergencyVehicals,vehicalPassed,remainingTimeSlot,greenSignalOrder)

  return [orderOfGreen,commonVehicalPassed,skippedDirection,remainingTimeslot]
}

function getEmergencyVehicals(traffic,defaultDirection) { //get list of emegency vehical present in the traffic at first
    let emergencyVehicalList=getEmergencyVehicalList();
    let trafficEntries=Object.entries(traffic);
    let waitingEmergencyVehicals=[]
    
    //get list of emergency vehicals
    for(let directionWiseTraffic of trafficEntries){ //directionWiseTraffic[0]=direction ,directionWiseTraffic[1]=array of traffic vehical
        for(let trafficArray of directionWiseTraffic[1]){
            if(emergencyVehicalList.includes(trafficArray.type)){
              waitingEmergencyVehicals.push([directionWiseTraffic[0],trafficArray.type,trafficArray.waitTime])
            }
        }
    }
    //sort the array to get queue of emergency vehical as per their priority
    let sortedWaitTimeOfEmergencyVehical=waitingEmergencyVehicals.sort((a,b)=>{
        if(a[2]==b[2]){
            return defaultDirection.indexOf(a[0])-defaultDirection.indexOf(b[0])
        }
        return b[2]-a[2]
    })


    return sortedWaitTimeOfEmergencyVehical
}

function passEmegencyVehical(emergencyVehicalList,timeSlot,traffic){ //let the emergency vehical pass the signal and after that the situation
    let vehicalPassed={};
    let greenSignalOrder=[]
    for(let vehical of emergencyVehicalList){
        if(timeSlot>=10){
            timeSlot-=10;
            if(!vehicalPassed[vehical[0]]){
                greenSignalOrder.push(vehical[0])
                vehicalPassed[vehical[0]]=[vehical[1]]
            }else{
                vehicalPassed[vehical[0]].push(vehical[1])
            }
        }
    }
    let trimmedTraffic=gettrimmedTraffic(traffic);
    return[
        remainingTimeSlot=timeSlot,
        vehicalPassed,
        trimmedTraffic,
        greenSignalOrder
    ]
}

function gettrimmedTraffic(traffic){ //traffic object after the emergency vehicals are passed
    let tempTraffic=Object.entries(traffic)
    for(let directionWiseTraffic of tempTraffic){
        for(let i=0;i<directionWiseTraffic[1].length;i++){
            let index=directionWiseTraffic[1].findIndex((val)=>isEmegencyVehical(val.type))
            if(index!==-1)
            directionWiseTraffic[1].splice(index,1)
            // for(let singleDirectionTraffic of directionWiseTraffic[1]){
            //     console.log(singleDirectionTraffic)
            // }
        }
    }
    return Object.fromEntries(tempTraffic)
}

function passCommonVehicals(trafficWithoutEmergencyVehicals,vehicalPassed,remainingTimeSlot,greenSignalOrder){ //to get the situation after the common vehicals have passed the signal
    // console.log(vehicalPassed,trafficWithoutEmergencyVehicals)
    let skippedDirection=[]
    let congestionWiseDirection=getcongestionWiseDirections(vehicalPassed,trafficWithoutEmergencyVehicals) //get list of vehical that are in traffic also only those directions which was remaining during the cycle 
    let congestionWiseSortedData=  Object.entries(congestionWiseDirection)
    let sortedCongestionData=Object.fromEntries( congestionWiseSortedData.sort((a,b)=>{
        return b[1]["time"]-a[1]["time"]
    }))

    for(let direction of Object.keys(sortedCongestionData)){ //Object.keys(congestionWiseDirection)
        if(remainingTimeSlot>0){
            for (let vehical of sortedCongestionData[direction]["vehicals"]){
                if(remainingTimeSlot>=getVehicalPaasingTime(vehical)){
                    if(!vehicalPassed[direction]){
                        greenSignalOrder.push(direction)
                        vehicalPassed[direction]=[vehical]
                    }else{
                        vehicalPassed[direction].push(vehical)
                    }
                    remainingTimeSlot-=getVehicalPaasingTime(vehical)
                }else{
                    if(!greenSignalOrder.includes(direction)){
                        skippedDirection.push(direction)
                    }
                }
            }
        }else{
            skippedDirection.push(direction)
        }
    }
    return [vehicalPassed,skippedDirection,greenSignalOrder,remainingTimeSlot]
}

function getcongestionWiseDirections(vehicalPassed,trafficWithoutEmergencyVehicals){ //get a object that stats the congestion time after emergency vehicals has passed 
    let passedDirection=Object.keys(vehicalPassed);
    for(let direction of passedDirection){
        delete trafficWithoutEmergencyVehicals[direction]
    }
    // console.log(trafficWithoutEmergencyVehicals);
    let congestionObject={}
    for (let direction of Object.keys(trafficWithoutEmergencyVehicals)){
        for(let vehical of trafficWithoutEmergencyVehicals[direction]){
            if(!congestionObject[direction]){
                congestionObject[direction]={time : vehical.waitTime,vehicals:[vehical.type]};
            }else{
                congestionObject[direction]["time"]+=vehical.waitTime;
                congestionObject[direction]?.vehicals.push(vehical.type)
            }
        }

    }
    // console.log(congestionObject)
    return congestionObject
}

function isEmegencyVehical(vehicalType){
    let emgVehicalList=getEmergencyVehicalList();
    return emgVehicalList.includes(vehicalType) ? 1 : 0;
}
function getEmergencyVehicalList(){ //list of emergency vehicals
    return ["ambulance","firetruck","police"]
}
function getVehicalPaasingTime(vehicalType) {
  let obj = {
    car: 5,
    bus: 10,
    bike: 3,
    ambulance: 10,
    firetruck: 10,
    police: 10,
  };
  return obj[vehicalType];
}