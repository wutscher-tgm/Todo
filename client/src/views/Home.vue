<template>
  <div id="home" class="fullheight">
    <div>
      <input type="text" v-model="listName">
      <input type="button" v-on:click="addList()" name="" id="">
    </div>
    <vue-custom-scrollbar class="scroll-area columns">
      <List class="column is-one-fifth tlist" v-for="(list, index) in lists" v-bind:key="index" v-bind:data="list"/>
    </vue-custom-scrollbar>
  </div>
</template>

<script>
import List from '@/components/List.vue'
import axios from 'axios'
import vueCustomScrollbar from 'vue-custom-scrollbar'

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
    List, vueCustomScrollbar
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
.scroll-area {
  position: relative;
  margin: auto;
  width: 100vw;
  height: 100%;
}
.fullheight{
  height: 100%;
}
.tlist{
  height: 200px;
}
</style>
