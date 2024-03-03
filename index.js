< !DOCTYPE html >
    <
    html >
    <
    head >
    <
    title > Web Real - Time Chat < /title> <
style >
    /* Add your CSS styles here */
    <
    /style> < /
head > <
    body >
    <
    div id = "messages" > < /div> <
form id = "message-form" >
    <
    input type = "text"
id = "message-input" / >
    <
    button type = "submit" > Send < /button> < /
form > <
    script src = "/socket.io/socket.io.js" > < /script> <
script >
    const socket = io();
const messagesDiv = document.getElementById('messages');
const messageForm = document.getElementById('message-form');
const messageInput = document.getElementById('message-input');

messageForm.addEventListener('submit', (e) => {
    e.preventDefault();
    if (messageInput.value) {
        socket.emit('send message', {
            room: 'your-room-id',
            message: messageInput.value,
        });
        messageInput.value = '';
    }
});

socket.on('new message', (message) => {
    const messageElement = document.createElement('p');
    messageElement.textContent = message;
    messagesDiv.appendChild(messageElement);
}); <
/script> < /
body > <
    /html>
