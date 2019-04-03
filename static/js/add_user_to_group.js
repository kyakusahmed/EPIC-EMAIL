let token = localStorage.getItem("token")

var select_form = document.getElementById('select_form')

select_form.addEventListener('submit', function(event){
    //prevent pager load
    event.preventDefault()

    var email = document.getElementById('group').value
    var group_id = document.getElementById('id').value

    fetch('http://127.0.0.1:5000/api/v1/groups/'+ group_id +'/users', {
        method:'POST',
        headers: {
            'Content-Type' : 'application/json',
            'Authorization': `Bearer ${localStorage.getItem("token")}`
        },
        body:JSON.stringify({
            'email': email
        })
    })
    .then(function(response){
        return response.json()
    })
    .then(function(response){
        if (response.status === 201) {
            alert("user added")
            window.location.replace("./ad-grp.html")
        }
        if (response.errors) {
            document.getElementById("add").innerHTML = response.errors
        }
        if (response.message === "unable to find user") {
            document.getElementById("add").innerHTML = "unable to find user"
        }
        if (response.msg) {
            alert("Missing Authorization Header")
        }
    })
    .catch(function(error){
        console.log(error)
    })

    
})