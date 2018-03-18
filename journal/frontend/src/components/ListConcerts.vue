
<template>
  <div class="container is-fluid">
    <h1><b>Concerts</b></h1>
    <ul>
      <li v-for="concert in concerts" >
        <router-link v-bind:to="'/journal/concerts/edit/' + getDate(concert.date)">
          {{ concert.name + " | " + concert.venue + " - " + concert.date }}
        </router-link>
        <ul>
          <li v-for="artist in artists" >
            <template v-if="concert.date === artist.concert.date">
              {{ artist.name }}
            </template>
          </li>
        </ul>
      </li>
    </ul>

  </div>
</template>

<script>
  export default {
  name: 'ListConcerts',
  methods: {
    getDate (pub_date) {
      let date = new Date(pub_date);
      let month = date.getMonth() + 1;
      let day = date.getUTCDate();
      let year = date.getFullYear();
      return month + "/" + day + "/" + year;
    }
  },
  computed: {
    concerts() {
      return this.$store.state.concerts;
    },
    artists() {
      return this.$store.state.artists;
    }
  },
  created() {
    if (this.$store.state.concerts === null) {
      this.$store.dispatch('fetchConcerts');
      this.$store.dispatch('fetchArtists');
    }
  },
}
</script>

<style scoped>

</style>

