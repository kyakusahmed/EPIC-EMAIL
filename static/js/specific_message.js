window.onload = function(){
    let my_url = location.href
    let url = new URL(my_url)
    let message_id = url.searchParams.get('message_id')
    get_specific(message_id)
}

var form = document.getElementById('read-form')

function get_specific(message_id) {
    let token = localStorage.getItem("token");

    fetch('https://epemail.herokuapp.com/api/v1/messages/' + message_id, {
        
        method: "GET",
        headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`
        }
    })
        .then(function(response) {
        return response.json();
        })
        .then(function(response) {
        if (response.status === 404) {
            console.log('response.error')
            document.getElementById.innerHTML = response.error
        }
            
        })
        .catch(error => {
        console.log(error);
        });
    };
