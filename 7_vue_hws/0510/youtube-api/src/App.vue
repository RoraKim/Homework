<template>
  <div id="app">
    <h1>My First Youtube Project</h1>
    <the-search-bar
      @input-search="onInputSearch"
    ></the-search-bar>
    <video-list
      :videos="videos"
    ></video-list>
  </div>
</template>

<script>
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'


import axios from 'axios'
import TheSearchBar from './components/TheSearchBar.vue'
import VideoList from './components/VideoList.vue'

export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoList
  },
  data() {
    return {
      searchKeyword: null,
      videos: [],
    }
  },
  methods: {
    onInputSearch(keyword) {
      this.searchKeyword = keyword
      const params = {
        part: 'snippet',
        type: 'video',
        key: API_KEY,
        q: this.searchKeyword
      }
      axios.get(API_URL,{params})
        .then(res => {
          console.log(res.data)

          this.videos = res.data.items
          console.log(this.videos)
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
