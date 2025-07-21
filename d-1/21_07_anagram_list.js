// Q2. Check if Two Lists are Anagrams
// Task: Write a function to check if two lists are anagrams or not.
// Examples:
// [1,2,3,2] and [2,1,3,2] → True
// [1,2,3] and [1,2,4] → False

// start time : 11:37
// end time : 12:15

let arr1=[1,4,3];
let arr2=[3,4,2];

function isAnagram(arr1,arr2){
    let flag=0,repeatingElements=[]
    if(arr1.length!=arr2.length){
        return false
    }
    for(let ele of arr1){
        if(arr1.indexOf(ele)!=arr1.lastIndexOf(ele) && !repeatingElements.includes(ele)){
            let count1=0;
            let count2=0;
            arr1.map((val)=>{
                if(val==ele){
                    count1++;
                }
            })
            arr2.map((val)=>{
                if(val==ele){
                    count2++;
                }
            })
            if(count1==count2){
                repeatingElements.push(ele)
                flag=1;
            }else{
                return false
            }
        }else{
            if(arr2.indexOf(ele)==-1){
                return false
            }else{
                flag=1
            }
        }
    }
    
    return flag ? true : false 
}

console.log(isAnagram(arr1,arr2))