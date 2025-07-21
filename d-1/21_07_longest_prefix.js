// Write a function to find the longest common prefix string amongst an array of strings.
// If there is no common prefix, return an empty string "".
// Example 1:
// Input: strs = ["flower","flow","flight"]
// Output: "fl"
// Example 2:
// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.

//strt time=10:50
//end time=11:23

let arr1=['fligth',"flower","low"];
let arr2=["dog","oracecar","dcar"];

function findLongestPrefix(arr){
    let flag=0;
    let longestPrefix=''
       for(let val1 of arr[0].split('')){
        longestPrefix+=val1
            for(let val of arr){
                val.startsWith(longestPrefix) ? flag=1 : flag=0;
                if(!flag){
                    if(longestPrefix.length==1){
                        return "There is no common prefix among the input strings"
                    }else{
                        return longestPrefix.split('').slice(0,longestPrefix.split('').length-1).join('')
                    }
                }
            }
        }
    return longestPrefix
}

console.log("answer :",findLongestPrefix(arr1))
console.log("answer :",findLongestPrefix(arr2))