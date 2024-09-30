<template>
  <div class="chatbot-container">
    <div class="chat-window">
      <div v-for="(message, index) in messages" :key="index" :class="['message', message.type]">
        {{ message.text }}
      </div>
    </div>

    <div class="chat-input">
      <input
        v-model="userMessage"
        @keyup.enter="sendMessage"
        type="text"
        placeholder="Type a message..."
      />
      <button @click="sendMessage">Send</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userMessage: "",
      messages: [
        { text: "Hello! How can I help you?", type: "bot" },
      ],
    };
  },
  methods: {
    sendMessage() {
      if (this.userMessage.trim() === "") return;

      // Add user message to chat
      this.messages.push({
        text: this.userMessage,
        type: "user",
      });

      // Clear input
      const userMessage = this.userMessage;
      this.userMessage = "";

      // Simulate bot response
      setTimeout(() => {
        this.messages.push({
          text: `You said: ${userMessage}`,
          type: "bot",
        });
      }, 1000);
    },
  },
};
</script>

<style scoped>
.chatbot-container {
  display: flex;
  flex-direction: column;
  height: 400px;
  width: 300px;
  border: 1px solid #ddd;
  border-radius: 10px;
  padding: 10px;
}

.chat-window {
  flex: 1;
  overflow-y: auto;
  padding-bottom: 10px;
  border-bottom: 1px solid #ddd;
}

.message {
  padding: 8px 10px;
  margin: 5px 0;
  border-radius: 5px;
  max-width: 80%;
}

.message.user {
  background-color: #d4f1f4;
  align-self: flex-end;
}

.message.bot {
  background-color: #f1f1f1;
  align-self: flex-start;
}

.chat-input {
  display: flex;
  margin-top: 10px;
}

.chat-input input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.chat-input button {
  padding: 10px;
  border: none;
  background-color: #4CAF50;
  color: white;
  cursor: pointer;
  margin-left: 5px;
}

.chat-input button:hover {
  background-color: #45a049;
}
</style>
