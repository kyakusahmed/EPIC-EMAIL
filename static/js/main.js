// var signup_form = document.getElementById('signup_form')

// signup_form.addEventListener('submit', function(event){
//     //prevent pager load
//     event.preventDefault()

//     var firstname = document.getElementById('firstname').value
//     var lastname = document.getElementById('lastname').value
//     var email = document.getElementById('email').value
//     var password = document.getElementById('password').value

//     fetch('http://127.0.0.1:5000/api/v1/messages', {
//         method:'GET',
//         headers: {'Content-Type' : 'application/json'},
//         body:JSON.stringify({
//             firstname: firstname,
//             lastname: lastname,
//             email: email,
//             password: password
//         })
//     })
//     .then(function(response){
//         return response.json()
//     })
//     .then(function(response){
//         if (response.message) {
//             document.getElementById("add").innerHTML = response.message
//             window.location.replace('../templates/signin.html')
//         } else if (response.error) {
//             document.getElementById("add").innerHTML = response.error
//         }
//     })
//     .catch(function(error){
//         console.log(error)
//     })

    