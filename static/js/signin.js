var login_form = document.getElementById('login_form')

login_form.addEventListener('submit', function(event){
    //prevent pager load
    event.preventDefault()

    var email = document.getElementById('email').value
    var password = document.getElementById('password').value

    fetch('https://epemail.herokuapp.com/api/v1/auth/login', {
        method:'POST',
        headers: {'Content-Type' : 'application/json'},
        body:JSON.stringify({
            email: email,
            password: password
        })
    })
    .then(function(response){
        return response.json()
    })
    .then(function(response){
        console.log(response)
        if (response.data[0]['access_token']) {
            alert(response.data[0]['access_token'])
            // window.location.replace('../templates/main.html')
            let token = response.data[0]['access_token']
            localStorage.setItem("token", token)
        } else if (response.error) {
            document.getElementById("add").innerHTML = response.error
        } 
    })
    .catch(function(error){
        console.log(error)
    })

    
})