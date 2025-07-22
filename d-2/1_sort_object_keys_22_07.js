// Given a object A, return a new object where the keys remain the same, but the values are sorted in ascending order. Assume that the dictionary values are either all integers or all strings (no mixed types like "1A2B").
// A = {"a": 1, "b": 3, "c": 2}
// # Output: {"a": 1, "c": 2, "b": 3}

// A = {"a": "B", "b": "C", "c": "A"}
// # Output: {"a": "A", "b": "B", "c": "C"}

//start time : 10:27
//end time : 10:44

let obj = {"a": 1, "b": 3, "c": 2}
// let obj={"b": 2,"d":"a","e":3, "a": "A", "c": 1,"f":"B"}

function getSortedKeysObject(obj){
    let sorted;
    let temp=Object.entries(obj);
    let tempObj={}
    //to sort mixed value of numbers and aplhabets (1A2aB)
    // sorted=temp.sort((a,b)=>{
    //     return a[1].toString().charCodeAt(0)-b[1].toString().charCodeAt(0)
    // })

    if(typeof temp[0][1]=="number"){
        //  sorted=temp.sort((a,b)=>{
        //     return a[1]-b[1]
        // })

        for(let i=0;i<temp.length;i++){
            for(let j=0;j<temp.length-1;j++){                
                if(temp[j][1]>temp[i][1]){
                    let t=temp[j];
                    temp[j]=temp[i];
                    temp[i]=t
                }
            }
        }
        sorted=temp

    }else{
        //  sorted=temp.sort((a,b)=>{
        //     return a[1].charCodeAt(0)-b[1].charCodeAt(0)
        // })
        for(let i=0;i<temp.length;i++){
            for(let j=0;j<temp.length-1;j++){                
                if(temp[j][1].toString().charCodeAt(0)>temp[i][1].toString().charCodeAt(0)){
                    let t=temp[j];
                    temp[j]=temp[i];
                    temp[i]=t
                }
            }
        }
    }
    return Object.fromEntries(temp)
}

console.log(getSortedKeysObject(obj))
