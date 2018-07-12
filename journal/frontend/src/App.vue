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
      this.$store.dispatch('fetchEntries');
      this.$store.dispatch('fetchConcerts');
      this.$store.dispatch('fetchArtists');
      this.$store.dispatch('fetchVenues');
      this.$store.dispatch('fetchActivities');
  },
}
</script>

<style>
#app {
}
</style>
