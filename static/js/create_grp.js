let token = localStorage.getItem("token")
var create_group = document.getElementById('create_group')

create_group.addEventListener('submit', function(event){
    //prevent pager load
    event.preventDefault()

    var group_name = document.getElementById('group').value

    fetch('https://epemail.herokuapp.com/api/v1/groups', {
        method:'POST',
        headers: {
            'Content-Type' : 'application/json',
            'Authorization': `Bearer ${localStorage.getItem("token")}`
        },
        body:JSON.stringify({
            group_name: group_name
        })
    })
    .then(function(response){
        return response.json()
    })
    .then(function(response){
        if (response.status === 201) {
            document.getElementById("add").innerHTML = "group added"
            window.location.replace("./ad-grp.html")
        }
        if (response.errors) {
            document.getElementById("add").innerHTML = response.errors
        }
        if (response.message === "Recipient does not exist") {
            document.getElementById("add").innerHTML = "Recipient does not exist"
        }
        if (response.msg) {
            document.getElementById("add").style.display = "block";
            document.getElementById("add").innerHTML = "Missing Authorization Header"
        }
    })
    .catch(function(error){
        console.log(error)
    })

    
})