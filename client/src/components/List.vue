<template>
  <div class="home">
    <Card msg="Welcome to Your Vue.js App"/>
    <textarea v-model="msg"/>
    <vue-markdown v-bind:source="msg"></vue-markdown>
  </div>
</template>

<script>
import Card from '@/components/Card.vue'
import VueMarkdown from 'vue-markdown'


export default {
  name: 'home',
  data(){
    return {
      msg: "# Test"
    }
  },
  components: {
    Card, VueMarkdown
  }
}
</script>
