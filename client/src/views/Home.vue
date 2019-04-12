<template>
  <div class="home">
    <List v-for="(list, index) in lists" v-bind:key="index" v-bind:data="list"/>
    <div>
      <input type="text" v-model="listName">
      <input type="button" v-on:click="addList()" name="" id="">
    </div>
  </div>
</template>

<script>
import List from '@/components/List.vue'
import axios from 'axios'

export default {
  name: 'home',
  data(){
    return {
      msg: "# Test",
      lists: [],
      listName: null
    }
  },
  components: {
    List
  },
  methods:{
    getLists(){
      axios.get('http://localhost:5000/list/').then(res=>{
        this.lists = res.data;
      })
    },
    addList(){
      axios.post('http://localhost:5000/list/', {
        title: this.listName
      }).then(res=>{
        this.getLists()
      })
    }
  },
  created(){
    this.getLists();
  }
}
</script>
