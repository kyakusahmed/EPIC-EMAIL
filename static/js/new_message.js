let token = localStorage.getItem("token")
var new_message = document.getElementById('new_message')

new_message.addEventListener('submit', function(event){
    //prevent pager load
    event.preventDefault()

    var subject = document.getElementById('subject').value
    var message = document.getElementById('message').value
    var receiver_email = document.getElementById('To').value

    fetch('http://127.0.0.1:5000/api/v1/messages', {
        method:'POST',
        headers: {
            'Content-Type' : 'application/json',
            'Authorization': `Bearer ${localStorage.getItem("token")}`
        },
        body:JSON.stringify({
            subject: subject,
            message: message,
            parentMessageID: 0,
            status: "sent",
            receiver_email: receiver_email
        })
    })
    .then(function(response){
        return response.json()
    })
    .then(function(response){
        if (response.status === 201) {
            alert("message sent")
        }
        if (response.errors) {
            document.getElementById("negative").innerHTML = response.errors
        }
        if (response.message === "Recipient does not exist") {
            document.getElementById("negative").innerHTML = "Recipient does not exist"
        }
        if (response.msg) {
            alert("Missing Authorization Header")
        }
    })
    .catch(function(error){
        console.log(error)
    })

    
})