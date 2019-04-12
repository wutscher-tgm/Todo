<template>
  <div class="home">
    <List/>
  </div>
</template>

<script>
import List from '@/components/List.vue'


export default {
  name: 'home',
  data(){
    return {
      msg: "# Test"
    }
  },
  components: {
    List
  }
}
</script>
