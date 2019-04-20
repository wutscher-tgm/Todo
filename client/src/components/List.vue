<template>
  <div class="todo-list">
    <!--List: {{data}}-->
    <div class="card">
      <header class="card-header">
        <p class="card-header-title is-size-3">
          {{data.title}}
        </p>
        <a href="#" class="card-header-icon">
          <input type="button" class="button is-primary is-rounded" v-on:click="isCreating=true" value="Create New">
        </a>
      </header>

      <vue-custom-scrollbar class="scroll-area card-content">
        <Card v-for="(todo, index) in data.todos" v-bind:key="index" v-bind:data="todo" style="padding:10px"/>
      </vue-custom-scrollbar>
    </div>

    <div v-bind:class="{ 'is-active': isCreating, 'modal': true }">
      <div class="modal-background"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">New Todo in <b>{{data.title}}</b></p>
          <button class="delete" v-on:click="isCreating=false"></button>
        </header>
        <section class="modal-card-body">

          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <label class="label">Title</label>
            </div>
            <div class="field-body">
              <div class="field">
                <p class="control">
                  <input class="input" type="text" placeholder="Todo Title ..." v-model="addTitle">
                </p>
              </div>
            </div>
          </div>

          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <label class="label">Description</label>
            </div>
            <div class="field-body">
              <div class="field">
                <p class="control">
                  <textarea class="textarea" placeholder="Describe the Todo ..." rows="10" v-model="addDesc" />
                </p>
              </div>
            </div>
          </div>

        </section>
        <footer class="modal-card-foot">
          <button class="button is-success" v-on:click="addItem(); isCreating=false">Save changes</button>
          <button class="button" v-on:click="isCreating=false">Cancel</button>
        </footer>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Card from '@/components/Card.vue'
import vueCustomScrollbar from 'vue-custom-scrollbar'

export default {
  name: 'home',
  props:[
    'data'
  ],
  data(){
    return {
      msg: "# Test",
      listId: null,
      isCreating: false,
      addDesc: null,
      addTitle: null
    }
  },
  components: {
    Card, vueCustomScrollbar
  },
  methods:{
    addItem(){
      axios.post('http://localhost:5000/item/'+this.data.id+'/', {
        item: {
          "title": this.addTitle,
          "desc": this.addDesc
        }
      },{
        'Content-Type': 'application/json'
      }).then(res=>{
        this.$parent.$parent.getLists()
      })
    }
  }
}
</script>
<style lang="scss" scoped>
.scroll-area {
  position: relative;
  margin: auto;
  width: 100%;
  height: 80%;
}
</style>
