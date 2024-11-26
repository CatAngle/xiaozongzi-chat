document.addEventListener('DOMContentLoaded', () => {
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');
    const chatMessages = document.querySelector('.chat-messages');
    const typingIndicator = document.querySelector('.typing-indicator');

    function addMessage(content, isUser = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user' : ''}`;
        
        const avatar = document.createElement('div');
        avatar.className = isUser ? 'user-avatar' : 'hamster-avatar';
        avatar.textContent = isUser ? '👤' : '🐹';
        
        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        messageContent.textContent = content;
        
        if (isUser) {
            messageDiv.appendChild(messageContent);
            messageDiv.appendChild(avatar);
        } else {
            messageDiv.appendChild(avatar);
            messageDiv.appendChild(messageContent);
        }
        
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    async function sendMessage() {
        const message = messageInput.value.trim();
        if (!message) return;

        // Add user message
        addMessage(message, true);
        messageInput.value = '';

        // Show typing indicator
        typingIndicator.classList.add('active');

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            
            // Hide typing indicator
            typingIndicator.classList.remove('active');
            
            // Add hamster's response
            addMessage(data.response);
            
        } catch (error) {
            console.error('Error:', error);
            typingIndicator.classList.remove('active');
            addMessage('啊哦，我好像遇到了一点小问题...让我休息一下下～');
        }
    }

    // Send message on button click
    sendButton.addEventListener('click', sendMessage);

    // Send message on Enter key
    messageInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Add welcome message
    addMessage('吱吱！我是小粽子，很高兴认识你！\n和我聊天吧，我可以给你讲很多有趣的故事哦～');
});
