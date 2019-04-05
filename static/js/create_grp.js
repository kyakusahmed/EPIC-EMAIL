let token = localStorage.getItem("token");
let email = localStorage.getItem("email");
var create_group = document.getElementById("create_group");
address.innerHTML = localStorage.getItem('email')

create_group.addEventListener("submit", function(event) {
  //prevent pager load
  event.preventDefault();

  var group_name = document.getElementById("group").value;

  fetch("https://epemail.herokuapp.com/api/v1/groups", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("token")}`
    },
    body: JSON.stringify({
      group_name: group_name
    })
  })
    .then(function(response) {
      return response.json();
    })
    .then(function(response) {
      address.innerHTML = localStorage.getItem('email')
      if (response.status === 201) {
        document.getElementById("postive").innerHTML = "group added";
        window.location.replace("./ad-grp.html");
      }
      if (response.errors) {
        document.getElementById("negative").innerHTML = response.errors;
      }
      if (response.message === "Recipient does not exist") {
        document.getElementById("negative").innerHTML =
          "Recipient does not exist";
      }
      if (response.msg) {
        document.getElementById("add").style.display = "block";
        document.getElementById("negative").innerHTML =
          "Missing Authorization Header";
      }
    })
    .catch(function(error) {
      console.log(error);
    });
});
