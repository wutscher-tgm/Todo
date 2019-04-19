<template>
  <div id="card">
    <div class="card">
      <div class="card-content">
        <p class="title">
          {{data.title}}  
        </p>
      </div>
      <footer class="card-footer">
        <a href="#" class="card-footer-item">Save</a>
        <a href="#" class="card-footer-item">Edit</a>
        <a href="#" class="card-footer-item">Delete</a>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Card',
  props: ['data']
}
</script>

<style lang="scss" scoped>
</style>
