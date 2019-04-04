var login_form = document.getElementById('login_form')

login_form.addEventListener('submit', function(event){
    //prevent pager load
    event.preventDefault()

    var email = document.getElementById('email').value
    var password = document.getElementById('password').value

    fetch('http://127.0.0.1:5000/api/v1/auth/login', {
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
        if (response.error){
            document.getElementById("negative").innerHTML = response.error
        } else if (response.data[0]['access_token']){
            console.log(response.data[0]['access_token'])
            alert(response.message)
            window.location.replace("./main.html")
            let token = response.data[0]['access_token']
            localStorage.setItem("token", token)
        }
    }) 
    
    })
        