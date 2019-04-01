var signup_form = document.getElementById('signup_form')

signup_form.addEventListener('submit', function(event){
    //prevent pager load
    event.preventDefault()

    var firstname = document.getElementById('firstname').value
    var lastname = document.getElementById('lastname').value
    var email = document.getElementById('email').value
    var password = document.getElementById('password').value

    fetch('https://epemail.herokuapp.com/api/v1/auth/signup', {
        method:'POST',
        headers: {'Content-Type' : 'application/json'},
        body:JSON.stringify({
            firstname: firstname,
            lastname: lastname,
            email: email,
            password: password
        })
    })
    .then(function(response){
        return response.json()
    })
    .then(function(response){
        if (response.message) {
            document.getElementById("add").innerHTML = response.message
            window.location.replace('../templates/signin.html')
        } else if (response.error) {
            document.getElementById("add").innerHTML = response.error
        }
    })
    .catch(function(error){
        console.log(error)
    })

    
})