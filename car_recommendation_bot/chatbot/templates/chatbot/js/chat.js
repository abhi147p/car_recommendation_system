document.querySelector('#send-button').onclick = function() {
    const message = document.querySelector('#user-input').value;
    fetch('/chatbot/webhook/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: message }),
    })
    .then(response => response.json())
    .then(data => {
        document.querySelector('#chat-box').innerHTML += `<p>${data.fulfillmentText}</p>`;
    });
};