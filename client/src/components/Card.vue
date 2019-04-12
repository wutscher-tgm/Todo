<template>
  <div class="hello">
    Item: {{data}}
  </div>
</template>

<script>
export default {
  name: 'Card',
  props: {
    data: String
  }
}
</script>