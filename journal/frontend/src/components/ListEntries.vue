
<template>
  <div class="container is-fluid">
    <h1><b>Journal Entries</b></h1>
    <ul>
      <li v-for="entry in entries" >
        <router-link v-bind:to="'/journal/entries/edit/' + getDate(entry.pub_date)">
          {{ getDate(entry.pub_date)}}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
  export default {
  name: 'ListEntries',
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
    entries() {
      return this.$store.state.entries;
    }
  },
  created() {
    if (this.$store.state.entries === null) {
      this.$store.dispatch('fetchEntries');
    }
  },
}
</script>

<style scoped>

</style>

