let token = localStorage.getItem("token");

var whole = document.getElementById("whole");

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

        for (let item of response.messages_received) {
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

      }
    })
    .catch(error => {
      console.log(error);
    });
});
