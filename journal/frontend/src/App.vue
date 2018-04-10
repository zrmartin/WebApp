<template>
  <div id="app">
    <Navbar/>
    <router-view/>
  </div>
</template>

<script>
import Navbar from "./components/Navbar"

export default {
  name: 'App',
  components: {
    Navbar
  },
    created() {
    if (this.$store.state.entries === null) {
      this.$store.dispatch('fetchEntries');
      this.$store.dispatch('fetchConcerts');
      this.$store.dispatch('fetchArtists');
    }
  },
}
</script>

<style>
#app {
}
</style>
