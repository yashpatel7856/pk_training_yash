// Write a function that takes an array of elements and returns the element that appears most frequently.
// If there are multiple elements with the same highest frequency, return any one of them.

// Input: ["a", "b", "a", "c", "a", "b"]
// Output: "a"

// start time : 3:08
//end time : 3:23


let arr=[1, 1,1,"b", "a", "c", "a", "b"]

function getFrequentElemnet(arr){
    let frequencyObject={},
        maxFreq={"itemname":"",
                  "frequency":0
        }
    arr.map((val)=>{    
        if(!frequencyObject[val]){
            frequencyObject[val]=1
        }else{
            frequencyObject[val]++
        }
    })
    Object.entries(frequencyObject).map((val)=>{
        if(maxFreq.frequency<val[1]){
             maxFreq.itemname=val[0];
             maxFreq.frequency=val[1];
        }
    })
    return maxFreq
}

console.log(getFrequentElemnet(arr))