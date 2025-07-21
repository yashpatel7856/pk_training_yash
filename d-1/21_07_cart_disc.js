// Problem Statement: Advanced Shopping Cart System (Without Built-in Functions)

// Objective:
// Build a shopping cart system that calculates the final payable amount for a customer after applying item-level discounts, bundled offers, cart-wide discounts, optional coupons, and region-based tax. You must not use any JavaScript built-in methods (e.g., .toFixed(), .toLowerCase(), Math.floor(), forEach, reduce, etc.).

// Input:

// 1. Cart – an array of objects, where each object represents an item:
//    Example:
//    const cart = [
//    { name: "Laptop", price: 60000, quantity: 1 },
//    { name: "Mouse", price: 2000, quantity: 3 },
//    { name: "Keyboard", price: 4000, quantity: 2 },
//    { name: "Monitor", price: 15000, quantity: 1 }
//    ];

// 2. Coupon – an optional object with the following structure (can be null):
//    const coupon = { type: "percent", value: 5 };

//    - type: "percent" or "flat"
//    - value: number indicating discount value

// 3. regionTaxRate – a number representing the tax rate in decimal format:
//    const regionTaxRate = 0.12; // 12% tax



// Rules to Apply:

// 1. Item-Level Discount:

//    - If item quantity is greater than or equal to 3, apply a 5% discount on that item's total (after bundle adjustment).

// 2. Bundle Offer:

//    - For Mouse only: Buy 2 Get 1 Free (i.e., 3 items for the price of 2).
//    - Must handle manually, including case-insensitive comparison.

// 3. Cart-Level Tiered Discount (on discounted total):

//    - If total is greater than 100000 → 10% discount
//    - If total is greater than 50000 → 5% discount
//    - Otherwise → No discount

// 4. Coupon Discount (after all discounts, before tax):

//    - If type is "percent": subtract the percentage from the total.
//    - If type is "flat": subtract the flat amount.

// 5. Tax:

//    - Apply tax on the amount after all discounts and coupons.

// 6. Rounding:

//    - All monetary values must be rounded to 2 decimal places using manual logic (no .toFixed()).


// Expected Output:

// {
// subtotal: 91000,
// afterItemDiscount: 89900,
// afterCartDiscount: 85405,
// afterCoupon: 81135,
// afterTax: 90871.2,
// finalTotal: 90871.2
// }


// Output Fields Explained:

// subtotal: Total before any discounts
// afterItemDiscount: After bundle and quantity-based item discounts
// afterCartDiscount: After applying cart-level tiered discounts
// afterCoupon: After applying coupon code (flat or percent)
// afterTax: After applying region tax
// finalTotal: Final amount payable (rounded to 2 decimals)

//start time : 4:20 
// end time : 6:56


   const cart = [
   { name: "Laptop", price: 60000, quantity: 1 },
   { name: "mouse", price: 2000, quantity: 3 },
   { name: "Keyboard", price: 4000, quantity: 2 },
   { name: "Monitor", price: 15000, quantity: 1 }
   ];

const coupon = { type: "percent", value: 5 };

const regionTaxRate = 0.12;


console.log(generateInvoice(cart,coupon,regionTaxRate))

function generateInvoice(cart,coupon,tax){

    let subTotal = getSubtotal(cart);
    let bundledObject=getBundledObject(cart);
    let itemDiscount=getitemDiscount(bundledObject);
    let afterItemDiscount=(subTotal-itemDiscount);
    let afterCartDiscount=getAftercartDiscount(afterItemDiscount);
    let afterCouponDiscount=getAfterCouponDiscount(afterCartDiscount,coupon)
    let afterTax=getAfterTax(afterCouponDiscount,tax)

    return {
        subTotal :subTotal.toFixed(2),
        afterItemDiscount,
        afterCartDiscount,
        afterCouponDiscount,
        afterTax:afterTax.toFixed(2),
        finalTotal:afterTax.toFixed(2)
    }
    
}

function getSubtotal(items){
    let subTotal=0;
    for(let item of items){
        subTotal+=item.price*item.quantity;
        if(isBundleOfferAvailable(item.name)){ //add value of bundled item in the subtotal
            subTotal+=getBundleOfferSum(item)
        }
    }
    // console.log("something"+subTotal);
    return subTotal
}


function getBundleOfferSum(item,flag=0){ //set falg to 1 to get only the count of extra items
    let minBought=2,freeNumber=1;
    if(flag){
        return freeItemsCount=Math.floor(item.quantity/minBought);
        // let str=(item.quantity/minBought)+''
        // let freeItemsCount=Number(str.substring(0,str.indexOf('.')))
        // return freeItemsCount
    }else{
        if(item.quantity==0){
            return 0;
        }
        if(item.quantity>minBought){
            // let str=item.quantity/minBought+'';
            // let freeItemsCount=NUmber(str.substring(0,str.indexOf('.')))
            let freeItemsCount=Math.floor(item.quantity/minBought);
            let freeItemvalue=freeItemsCount*freeNumber*item.price;
            return freeItemvalue;
        }
    }
}

function getBundledObject(cart){
    let bundledCart=cart.map((val)=>{
        if(isBundleOfferAvailable(val.name)){
            val.quantity=val.quantity+getBundleOfferSum(val,1)
        }
        return val
    })
    return bundledCart
}

function isBundleOfferAvailable(itemName){
    let bundleOfferItemsName=['Mouse']
    // return bundleOfferItemsName.includes(itemName) ? 1 : 0;
    let flag=0;
    bundleOfferItemsName.map((val)=>{
        testRegex(val,itemName) ? flag=1 : flag=0;
    })
    return flag
}

function testRegex(name,test){
    let regex = new RegExp(name,"i")
    return regex.test(test);

}

function getitemDiscount(cart){ //this function return the amount of discount not the amount after the discount
    let discount=0
    cart.map((val)=>{
        if(val.quantity>=3){
            discount+= (val.quantity*val.price*0.05).toFixed(2);
        }
    })
    
    return Number(discount)
}

function getAftercartDiscount(afterDiscountValue){
    let cartDiscountObject={
        "100000":10,
        "50000":5
    }
    let temp=afterDiscountValue;
    Object.keys(cartDiscountObject).map((val)=>{
        if(afterDiscountValue>Number(val)){
             temp= afterDiscountValue- afterDiscountValue * cartDiscountObject[val]/100;
        }
    })
    return temp
}

function getAfterCouponDiscount(afterDiscountValue,couponCode){
    if(couponCode.type=="percent"){
        return afterDiscountValue - afterDiscountValue * couponCode.value/100
    }else{
        return afterDiscountValue-couponCode.value
    }
}

function getAfterTax(afterCouponDiscount,tax){
    return afterCouponDiscount+afterCouponDiscount*tax
}