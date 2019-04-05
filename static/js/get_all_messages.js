let token = localStorage.getItem("token");
let email = localStorage.getItem('email')

let whole = document.getElementById("whole");
let number = document.getElementById("number");
let address = document.getElementById("address")
address.innerHTML = localStorage.getItem('email')

document.addEventListener("DOMContentLoaded", function() {
  fetch("https://epemail.herokuapp.com/api/v1/messages/received", {
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
      if (response.messages_received) {
        let sentMailsDiv = document.getElementById("sent_mails");
        number.innerHTML = '(' + response.number + ')'
        address.innerHTML = localStorage.getItem('email')
        if (response.number < 1) {
          document.getElementById("postive").innerHTML = "you have no messages"
        }
        for (let item of response.messages_received) {
          let mailDiv = document.createElement("form");
          mailDiv.classList.add("main");
          mailDiv.innerHTML =
            '<div class="content" id="content" style="color: black">' +
            '<div class="title">' +
            item.subject +
            "</div>" +
            "</div>" +
            '<div class="content1" id="content1" style="color: black">' +
            '<div class="title">' +
            item.message +
            "</div>" +
            "</div>" +
            '<div class="order-button" >' +
            '<a href="#?messge_id=' +
            item.message_id +
            '" class="button">Read</a>' +
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
