<template>
  <div class="home">
    List: {{data}}
    <Card v-for="(todo, index) in data.todos" v-bind:key="index" v-bind:data="todo"/>
  </div>
</template>

<script>
import Card from '@/components/Card.vue'
import VueMarkdown from 'vue-markdown'
//<vue-markdown v-bind:source="msg"></vue-markdown>

export default {
  name: 'home',
  props:[
    'data'
  ],
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
