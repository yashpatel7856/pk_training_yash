// Given a object A, return a new object where the keys remain the same, but the values are sorted in ascending order. Assume that the dictionary values are either all integers or all strings (no mixed types like "1A2B").
// A = {"a": 1, "b": 3, "c": 2}
// # Output: {"a": 1, "c": 2, "b": 3}

// A = {"a": "B", "b": "C", "c": "A"}
// # Output: {"a": "A", "b": "B", "c": "C"}

//start time : 10:27
//end time : 10:44

let obj = {"a": "b", "b": "a", "c": "c"}
// let obj={"b": 2,"d":"a","e":3, "a": "A", "c": 1,"f":"B"}

function getSortedKeysObject(obj){
    let sorted;
    let temp=Object.entries(obj);
    
    //to sort mixed value of numbers and aplhabets (1A2aB)
    // sorted=temp.sort((a,b)=>{
    //     return a[1].toString().charCodeAt(0)-b[1].toString().charCodeAt(0)
    // })

    if(typeof temp[0][1]=="number"){
         sorted=temp.sort((a,b)=>{
            return a[1]-b[1]
        })
    }else{
         sorted=temp.sort((a,b)=>{
            return a[1].charCodeAt(0)-b[1].charCodeAt(0)
        })
    }
    return Object.fromEntries(sorted)
}

console.log(getSortedKeysObject(obj))
