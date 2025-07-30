// start time : 11:00
// end time : 5:50

console.log("script loaded");

let isfullNameValid=false,isuserNameValid=false,isPassValid=false,iscPassValid=false,isNumberValid=false,isSelectValid=false,isGenderValid=false
window.onload=(e)=>{
    setDate()
}

const showPassword=document.getElementById('showPassword');
showPassword.addEventListener("change",(e)=>{
    viewPassword();
})

let submitButton = document.getElementById("submit");
    submitButton.addEventListener("click",(e)=>{
        console.log(e)
    })

  const fullName = document.getElementById("fullName")
  fullName.addEventListener("blur",(e)=>{
        console.log(fullName.value);
        let isNameValid = false;
        isNameValid = validateName(fullName.value);
        let errorspan=fullName.nextSibling.nextSibling
        if (!isNameValid) {
            isfullNameValid=false
            fullName.style.borderColor="red"
            errorspan.style.display="block"
            errorspan.style.color="red"
            errorspan.innerHTML="Name should be only char"
            return
        }else{
            isfullNameValid=true
            fullName.style.borderColor="black"
            errorspan.style.display = "none";
            checkForSubmit()
        }
    })

  const userName = document.getElementById("username");
  userName.addEventListener("blur",(e)=>{
    let errorspan=userName.nextSibling.nextSibling
    if (!validateUserName(userName.value)) {
            userName.style.borderColor="red"
            isuserNameValid=false
            errorspan.style.display="block"
            errorspan.style.color="red"
            errorspan.innerHTML="user name should have atleast 6 alphanumeric chars"
            return
    }else{
        userName.style.borderColor="black"
        isuserNameValid=true
        errorspan.style.display = "none";
        checkForSubmit()
    }
  })

  const pass = document.getElementById("password");
  pass.addEventListener("input",(e)=>{
    let errorspan=pass.nextSibling.nextSibling
        if (!validatePass(pass.value)) {
            pass.style.borderColor="red"
            isPassValid=false
            errorspan.style.display="block"
            errorspan.style.color="red"
            errorspan.innerHTML="Easy to Crack Password (PassWord length should be atleast 8 ,its hould conatian atleast 1 Capital char,1 sign,1 Digit)"
            return
        }else{
            pass.style.borderColor="black"
            isPassValid=true
            errorspan.style.display = "block";
            errorspan.style.color="green"
            errorspan.innerHTML="Strong Password !!"
            checkForSubmit()
        }
    })

  const cpass = document.getElementById("cpassword");
  cpass.addEventListener("input",(e)=>{
    let errorspan=cpass.nextSibling.nextSibling
        if (pass.value != cpass.value) {
            cpass.style.borderColor="red"
            iscPassValid=false
            errorspan.style.display="block"
            errorspan.style.color="red"
            errorspan.innerHTML="Password and confirm password should match"
            return
        }else{
            cpass.style.borderColor="black"
            iscPassValid=true
            errorspan.style.display = "none";
            checkForSubmit()
        }
   })

  const phoneNumber = document.getElementById("phoneNumber");
  phoneNumber.addEventListener("blur",(e)=>{
    let errorspan=phoneNumber.nextSibling.nextSibling
        if(!validateNumber(phoneNumber.value)){
            phoneNumber.style.borderColor="red"
            isNumberValid=false
            errorspan.style.display="block"
            errorspan.style.color="red"
            errorspan.innerHTML="phone number should be of length 10 and all the numbers"
            return
        }else{
            phoneNumber.style.borderColor="black"
            isNumberValid=true
            errorspan.style.display = "none";
            checkForSubmit()
        }
    })

    const genderRadio=document.getElementById("radio")
    genderRadio.addEventListener("blur",(e)=>{
        let  errorspan=genderRadio.nextSibling.nextSibling
        console.log(genderRadio.value)
        
    })

    const selectCountry=document.getElementById("country")
    selectCountry.addEventListener("blur",(e)=>{
        let errorspan=selectCountry.nextSibling.nextSibling
        if(selectCountry.value>=1){
            selectCountry.style.borderColor="black"
            isSelectValid=true
            errorspan.style.display = "none";
            checkForSubmit()
        }else{
            selectCountry.style.borderColor="red"
            isSelectValid=false
            errorspan.style.display="block"
            errorspan.style.color="red"
            errorspan.innerHTML="Please select Nationality"
            return
        }
    })

function checkForSubmit(){
    if(isfullNameValid&&isuserNameValid&&isPassValid&&iscPassValid&&isNumberValid&&isSelectValid){
        let submitBtn=document.getElementById("submit")
        submitBtn.disabled=false
    }
}

function viewPassword() {
  var x = document.getElementById("password");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

function createErrorSpan(errMsg) {
  let span = document.createElement("span");
  span.innerHTML = errMsg;
  span.style.color = "red";
  return span;
}

function validateName(name) {
  let regex = /[A-Za-z]+/i;
  return regex.test(name) ? 1 : 0;
}

function validateUserName(username) {
  let regex = /^[a-zA-Z0-9]{6}$/;
  return regex.test(username) ? 1 : 0;
}

function validatePass(password){
    let regex= /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$/
    return regex.test(password) ? 1 : 0;
}

function validateNumber(number){
    let regex=/^[0-9]{10}$/
    return regex.test(number) ? 1 : 0
}

function setDate(){
        var dtToday = new Date();
    
        var month = dtToday.getMonth() + 1;
        var day = dtToday.getDate();
        var year = dtToday.getFullYear() - 18;
        if(month < 10)
            month = '0' + month.toString();
        if(day < 10)
            day = '0' + day.toString();
    	var minDate = year + '-' + month + '-' + day;
        var maxDate = year + '-' + month + '-' + day;
    	document.getElementById("dob").setAttribute('max', maxDate);

}