<template>
  <div id="app">
    <Chatbot />
  </div>
</template>

<script>
import Chatbot from './components/MyChatbot.vue';

export default {
  name: 'App',
  components: {
    Chatbot,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  margin-top: 40px;
}
</style>
