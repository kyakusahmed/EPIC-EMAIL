function logout() {
  localStorage.removeItem("token");
  window.location.replace('./signin.html');
}
window.onload = function check_login() {
  if (token === null) {
    window.location.replace("./signin.html")
  }
}

let token = localStorage.getItem("token");
let email = localStorage.getItem("email");
var whole = document.getElementById("whole");
var num = document.getElementById("num");
address.innerHTML = localStorage.getItem("email");

document.addEventListener("DOMContentLoaded", function() {
  fetch("https://epemail.herokuapp.com/api/v1/messages/sent", {
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
      if (response.messages_sent) {
        let sentMailsDiv = document.getElementById("sent_mails");
        num.innerHTML = "(" + response.num + ")";
        address.innerHTML = localStorage.getItem("email");
        if (response.num < 1) {
          document.getElementById("postive").innerHTML = "you have no messages"
        }
        for (let item of response.messages_sent) {
          let mailDiv = document.createElement("div");
          mailDiv.classList.add("main");
          mailDiv.innerHTML =
            '<div class="content" id="content">' +
            '<div class="title">' +
            item.subject +
            "</div>" +
            "</div>" +
            '<div class="content1" id="content1">' +
            '<div class="title">' +
            item.message +
            "</div>" +
            "</div>" +
            '<div class="order-button">' +
            '<a href="read.html?mail=' +
            item.message_id +
            '" class="button">sent</a>' +
            "</div>";
          sentMailsDiv.appendChild(mailDiv);
          console.log(item.message);
        }
      }
    })
    .catch(error => {
      console.log(error);
    });
});

