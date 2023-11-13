






// document.addEventListener("DOMContentLoaded", function() {
//     const chatbox = document.querySelector(".chatbox");
//     const inputField = chatbox.querySelector(".chatbox__footer input");
//     const sendButton = chatbox.querySelector(".chatbox__footer .send__button");
//     const messagesContainer = chatbox.querySelector(".chatbox__messages");
//     const chatboxIcon = document.querySelector(".chatbox-icon");
  
//     sendButton.addEventListener("click", function() {
//       const message = inputField.value;
//       if (message.trim() !== "") {
//         appendMessageToChatbox(message, true);
//         inputField.value = "";
//         sendMessageToServer(message);
//       }
//     });
  
//     chatboxIcon.addEventListener("click", function() {
//       chatbox.classList.toggle("open");
//     });
  
//     function appendMessageToChatbox(message, isUser) {
//       const messageDiv = document.createElement("div");
//       messageDiv.classList.add("message");
//       messageDiv.classList.add(isUser ? "user-message" : "bot-message");
//       messageDiv.textContent = message;
//       messagesContainer.appendChild(messageDiv);
//     }
  
//     function sendMessageToServer(message) {
//       fetch($SCRIPT_ROOT + "/chat", {
//         method: "POST",
//         headers: {
//           "Content-Type": "application/json"
//         },
//         body: JSON.stringify({ text: message })
//       })
//         .then(response => response.json())
//         .then(data => {
//           appendMessageToChatbox(data.text, false);
//         })
//         .catch(error => {
//           console.error("Error sending message to server:", error);
//         });
//     }
//   });
  





// onSendButton(chatbox) {
//     var textField = chatbox.querySelector('input');
//     let text1 = textField.value
//     if (text1 === "") {
//         return;
//     }

//     let msg1 = { name: "User", message: text1 }
//     this.messages.push(msg1);

//     fetch('/chat/', {  // Assuming the Django view URL is '/chat/'
//         method: 'POST',
//         body: JSON.stringify({ text: text1 }),  // Sending 'text' instead of 'message'
//         headers: {
//           'Content-Type': 'application/json'
//         },
//       })
//       .then(response => response.json())
//       .then(data => {
//         let msg2 = { name: "Sam", message: data.text };
//         this.messages.push(msg2);
//         this.updateChatText(chatbox)
//         textField.value = ''

//     }).catch((error) => {
//         console.error('Error:', error);
//         this.updateChatText(chatbox)
//         textField.value = ''
//       });
// }


















class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        }

        this.state = false;
        this.messages = [];
    }

    display() {
        const {openButton, chatBox, sendButton} = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox))

        sendButton.addEventListener('click', () => this.onSendButton(chatBox))

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }

    toggleState(chatbox) {
        this.state = !this.state;

        // show or hides the box
        if(this.state) {
            chatbox.classList.add('chatbox--active')
        } else {
            chatbox.classList.remove('chatbox--active')
        }
    }

    onSendButton(chatbox) {
        var textField = chatbox.querySelector('input');
        let text1 = textField.value
        if (text1 === "") {
            return;
        }

        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);

        fetch('http://127.0.0.1:8000/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
            },
          })
          .then(r => r.json())
          .then(r => {
            let msg2 = { name: "Sam", message: r.answer };
            this.messages.push(msg2);
            this.updateChatText(chatbox)
            textField.value = ''

        }).catch((error) => {
            console.error('Error:', error);
            this.updateChatText(chatbox)
            textField.value = ''
          });
    }

    updateChatText(chatbox) {
        var html = '';
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "Sam")
            {
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
            }
            else
            {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
            }
          });

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }
}


const chatbox = new Chatbox();
chatbox.display();