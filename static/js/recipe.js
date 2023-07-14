$(document).ready(function() {
    var chatbox = $('#chatbox');
    var chatForm = $('#chat-form');

    function displayMessage(message) {
        var messageElement = $('<div>').text(message);
        chatbox.append(messageElement);
    }

    function sendMessage(message) {
        $.get('/chatbot/process_message/', { message: message }, function(response) {
            var reply = response.message;
            displayMessage(reply);
        });
    }

    // Handle form submission
    chatForm.submit(function(event) {
        event.preventDefault();
        var userInput = 'User: ' + $('#user-input').val();
        displayMessage(userInput);
        sendMessage($('#user-input').val());
        $('#user-input').val('');
    });
});
