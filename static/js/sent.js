let token = localStorage.getItem("token");

var whole = document.getElementById("whole");

document.addEventListener("DOMContentLoaded", function() {
  fetch("http://127.0.0.1:5000/api/v1/messages/sent", {
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
            '" class="button">Read</a>' +
            "</div>";
          sentMailsDiv.appendChild(mailDiv);
          console.log(item.message);
        }
        // var contentDiv = document.getElementById('content')
        // contentDiv.innerHTML = `<div class="title">${response.messages_received[0]['subject']}</div>`;
      }
    })
    .catch(error => {
      console.log(error);
    });
});
