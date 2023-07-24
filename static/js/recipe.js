// HANDLES THE CHATBOT RESPONSE SYSTEM 

// $(document).ready(function() {
//     // let botMessage = $('#bot-message');
//     var mainChatbox = $('#main-chbot');
//     var chatForm = $('#chat-form');

//     function displayMessage(message) {
//         var messageElement = $('<p>').text(message);
//         mainChatbox.append(messageElement);
//     }

//     function sendMessage(message) {
//         $.get('/recipe/process_message/', { message: message }, function(response) {
//             var reply = response.message;
//             displayMessage(reply);
//         });
//     }

//     // Handle form submission
//     chatForm.submit(function(event) {
//         event.preventDefault();
//         var userInput =   $('#user-input').val() ;
//         displayMessage(userInput);
//         sendMessage($('#user-input').val());
//         $('#user-input').val('');
//     });
// });


// Written

let messBtn = document.getElementById("mess-btn");
let myFrom = document.getElementById("chat-form");


const submitFm = ()=>{
    myFrom.submit();
    console.log("searched");
}

messBtn.addEventListener("click", submitFm);

myFrom.addEventListener('keyup', function(event){
    if(event.code === 'Enter'){
        event.preventDefault();
        document.querySelector('form').submit();

    }
})


