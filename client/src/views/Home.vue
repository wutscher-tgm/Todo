<template>
  <div id="home">
    <div>
      <input type="text" v-model="listName">
      <input type="button" v-on:click="addList()" name="" id="">
    </div>

    <div class="columns scroll-x fullheight">
      <List class="column" v-for="(list, index) in lists" v-bind:key="index" v-bind:data="list"/>
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
      },{
        'Content-Type': 'application/json'
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
<style lang="scss" scoped>
.scroll-x{
  overflow-x: scroll
}
.fullheight{
  height: 100%;
}
#home{
  height: 100%;
}
</style>
