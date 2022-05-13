<template>
  <input type="text" @keyup.enter="onInputSearch">
</template>

<script>
export default {
  name: 'TheSearchBar',
  methods: {
    onInputSearch(event) {
      // console.log(event.target.value)
      this.$emit('input-search', event.target.value)
    }
  }
}
</script>

<style>

</style>