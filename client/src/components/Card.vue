<template>
  <div id="card">
    <div class="card">
      <!--<header class="card-header">
        <p class="card-header-title">
          {{data.title}}
        </p>
        <a href="#" class="card-header-icon" aria-label="more options">
          <span class="icon">
            <i class="fas fa-angle-down" aria-hidden="true"></i>
          </span>
        </a>
      </header>-->

      <a class="card-contentt" v-on:click="show()">
        <p class="card-header-title">
          {{data.title}}
        </p>
        <!--<vue-markdown v-bind:source="data.desc"></vue-markdown>-->
        <!--<Markdown v-bind:data="data.desc"/>-->
      </a>
      <footer class="card-footer">
        <a v-on:click="show()" class="card-footer-item">More</a>
        <a v-on:click="show(); editing=true" class="card-footer-item">Edit</a>
        <a href="#" class="card-footer-item">Delete</a>
      </footer>
    </div>




    <div v-bind:class="{ 'is-active': expand, 'modal': true }" @keydown.esc="hide()">
      <div class="modal-background" v-on:click="hide()"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">{{data.title}}</p>
          <button class="delete" v-on:click="hide()" aria-label="close"></button>
        </header>
        <section class="modal-card-body">
          <Markdown v-bind:data="data.desc"/>
        </section>
        <footer class="modal-card-foot">
          <button v-if="!editing" v-on:click="editing=true" class="button is-success">Edit</button>
          <button v-if="editing" v-on:click="edit()" class="button is-success">Save changes</button>
          <button class="button" v-on:click="cancel()">Cancel</button>
        </footer>
      </div>
    </div>
  </div>
</template>

<script>
import VueMarkdown from 'vue-markdown'
import Markdown from '@/components/Markdown.vue'

export default {
  name: 'Card',
  props: ['data'],
  components:{
    VueMarkdown, Markdown
  },
  data(){
    return {
      expand: false,
      editing: false
    }
  },
  methods:{
    alert(){
      alert('test')
    },
    show(){
      window.addEventListener('keydown', this.keyevent)
      this.expand=true
    },
    hide(){
      window.removeEventListener('keydown', this.keyevent)
      this.expand=false
    },
    edit(){

    },
    cancel(){

    },
    keyevent(event){
      if(event.code == 'Escape'){
        this.expand=false
      }
    }
  }
}
</script>

<style lang="scss" scoped>
</style>
