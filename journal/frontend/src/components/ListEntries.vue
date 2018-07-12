
<template>
  <div class="container is-fluid">
    <h1><b><u>Entries</u></b></h1>
    <ul>
      <li v-for="entry in entries" >
        <router-link v-bind:to="'/journal/entries/edit/' + getDate(entry.pub_date)">
          {{"Date Published: "  + getDate(entry.pub_date)}}
        </router-link>
        <ul>
          <li><b>Summary: </b>  {{entry.summary}}</li>
          <li>Activities:</li>
          <li v-for="activity in activities">
            <template v-if="getDate(entry.pub_date) === getDate(activity.entry['pub_date'])">
              {{activity.name + " for " + activity.duration + " Minutes"}}
            </template>
        </li>
        </ul>
        <br>
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
    },
    activities() {
      return this.$store.state.activities;
    }
  },
}
</script>

<style scoped>

</style>

