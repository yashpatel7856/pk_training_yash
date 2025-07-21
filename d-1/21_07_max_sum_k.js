// Write a function that takes an array of numbers and a number k, and returns the maximum sum of any k consecutive elements in the array.

// Input: [2, 1, 5, 1, 3, 2], k = 3
// Output: 9

// Input: [1, 9, -1, -2, 7, 3], k = 4
// Output: 13

// start time: 3:35
//end time : 3:51

function getMaxConsecutiveSum(arr,k){    
    if(k==0 || k>arr.length || k<0){
        return "enter number in range of array length"
    }
    let maxSum=0;
    arr.map((val,ind)=>{
        while(ind+k<=arr.length){
            let tempSum=0;
            for(let i=0 ;i<k;i++){
                tempSum+=arr[ind+i]
            }
            if( tempSum > maxSum ){
                maxSum=tempSum 
            }
            ind++;
        }
    })
    return maxSum
}
let arr1=[2, 1, 5, 1, 3, 2]
let arr2=[1, 9, -1, -2, 7, 3];

console.log(getMaxConsecutiveSum(arr1,1))