let token = localStorage.getItem("token");
let email = localStorage.getItem('email')

let whole = document.getElementById("whole");
let group = document.getElementById("grp");
let address = document.getElementById("address")
address.innerHTML = localStorage.getItem('email')
let post = document.getElementById("post")

document.addEventListener("DOMContentLoaded", function() {

    fetch("https://epemail.herokuapp.com/api/v1/groups", {
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
        console.log(response);
        
        if (response.groups) {
            let groupsMailsDiv = document.getElementById("sixth");

            grp.innerHTML = '(' + response.number + ')'

            address.innerHTML = localStorage.getItem('email')

            if (response.number < 1) {
                document.getElementById("post").innerHTML = "Currently, you are not part of any group"
            }
            for (let item of response.groups) {
            let mailDiv = document.createElement("div");
            mailDiv.classList.add("group_name");
            mailDiv.innerHTML =
            '<div class="groupname">' +
            '<p>' + item.group_name + '<span>' + '<a href="#">' + 
            '<input type="submit" value="Delete">' + '</a></span>'
            '</p>' + '</div>';
            groupsMailsDiv.appendChild(mailDiv);
            console.log(item.message);
            }
            
        }
        })
        .catch(error => {
        console.log(error);
        });
    });
