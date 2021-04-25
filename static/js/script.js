

function buttonSubmit(title,price){
    fetch('/config/')
    .then((res)=>{return res.json() })
    .then((data)=>{
        console.log(data)
          // Initialize Stripe.js
        const stripe =  Stripe(data.public_key)
        

    // Get the checkout Session ID
    fetch('/create-chkout-session/?title='+title+'&&price='+price)
        .then((result)=>{ return result.json() })
        .then((data)=>{
            console.log(data.sessionId)
            return stripe.redirectToCheckout({sessionId: data.sessionId})
        })
        .then((res)=>{
            console.log(res)
        })
    })


}
