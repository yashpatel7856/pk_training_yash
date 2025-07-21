// Find the longest contiguous increasing subsequence in an array of integers. The function should return the sub-list of the longest contiguous increasing subsequence in the provided array. The difference between consecutive integers must be the same while checking the increment. The minimum output length will be 3.
// Input: [1, 3, 5, 7, 4, 7, 0, 1, 2, 3, 4, 5, 6, 34, 44] 
// Output: [0, 1, 2, 3, 4, 5, 6]

//start time : 12:26
//end time : 3:03

//for any difference
let arr=[0,0,1,1] 
function longestSequence(arr){
    let contiguousIncrement=0;
    let longestSeqArray=[];
    for(let ind in arr){
            contiguousIncrement=Math.abs(arr[ind]-arr[Number(ind)+1]);
        if(Math.abs(arr[ind]-arr[Number(ind)+1])!=contiguousIncrement){
            continue;
        }else{
            let tempArray=[]
            while(ind<arr.length ){
                    if(Math.abs(arr[ind]-arr[Number(ind)+1])==contiguousIncrement || Math.abs(arr[ind]-arr[Number(ind)+1])==Math.abs(arr[ind]-arr[Number(ind)-1]) || Math.abs(arr[ind]-arr[Number(ind)-1])==contiguousIncrement){
                        tempArray.push(arr[ind]);
                    }
                    if(Math.abs(arr[ind]-arr[Number(ind)+1])!=contiguousIncrement){
                        break;
                    }
                ind++;
            }
            
            if(tempArray.length>longestSeqArray.length){
                longestSeqArray.splice(0,longestSeqArray.length,...tempArray)

            }
        }
    }
    return longestSeqArray
}
console.log(longestSequence(arr))


//for increment of one diff=1
// let arr=[1,2,3,4, 0, 1, 2,3,4,5,6, 7,8,34, 44] 
// function longestSequence(arr){
//     let markerFlag;
//     let isCountinious=0;
//     let longestSeqArray=[],longestSeqLength=0;
//     for(let ind in arr){
//         if(Math.abs(arr[ind]-arr[Number(ind)+1])!=1){
//             continue;
//         }else{
//             let tempArray=[]
//             while(ind<arr.length ){
//                     if(Math.abs(arr[ind]-arr[Number(ind)+1])==1 || Math.abs(arr[ind]-arr[Number(ind)-1])==1){
//                         tempArray.push(arr[ind]);
//                     }
//                     if(Math.abs(arr[ind]-arr[Number(ind)+1])!=1){
//                         break;
//                     }
//                 ind++;
//             }
            
//             if(tempArray.length>longestSeqArray.length){
//                 longestSeqArray.splice(0,longestSeqArray.length,...tempArray)

//             }
//         }
//     }
//     return longestSeqArray
// }

// console.log(longestSequence(arr))