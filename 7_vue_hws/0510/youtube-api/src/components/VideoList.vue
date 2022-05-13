<template>
  <ul>
    <li v-for="(video, idx) in videos" :key="idx">
      {{ video.snippet.title }}
    </li>
  </ul>
</template>

<script>
export default {
  name: 'VideoList',
  props: {
    videos: Array
  }

}
</script>

<style>

</style>