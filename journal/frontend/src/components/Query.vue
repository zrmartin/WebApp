<template>
  <div class="container is-fluid">


    <div class="field is-grouped">
      <div class="control">
        <button class="button" v-on:click="queryOne"> SELECT * FROM Venue </button>
      </div>
      <div class="control">
        <button class="button" v-on:click="queryTwo"> SELECT Name, Style FROM Venue </button>
      </div>
      <div class="control">
        <button class="button" v-on:click="queryThree"> SELECT Venue.name, Concert.name FROM Venue, Concert WHERE Venue.venueID = Concert.venueID </button>
      </div>
    </div>

    <div v-if="results1 !== undefined" v-for="result in results1">
      <p>{{result}}</p>
      <br>
    </div>

    <div v-if="results2 !== undefined" v-for="result in results2">
      <p>{"name": "{{result.name}}", "style": "{{result.style}}" }</p>
      <br>
    </div>

    <div v-if="results3 !== undefined" v-for="result in results3">
      <p>{"Venue.name": "{{result.venue.name}}", "Concert.name": "{{result.name}}" }</p>
      <br>
    </div>

  </div>

</template>

<script>
    const api = "http://localhost:8000";
    import axios from 'axios';
    export default {
      name: "Query",
      data() {
        return {
          results1: undefined,
          results2: undefined,
          results3: undefined,
        }
      },
      methods: {
        queryOne() {
          let vm = this;
          vm.results2 = undefined;
          vm.results3 = undefined;
          axios.get(api + "/journal/query1")
            .then(response => {
              vm.results1 = response.data;
            })
        },
        queryTwo() {
          let vm = this;
          vm.results1 = undefined;
          vm.results3 = undefined;
          axios.get(api + "/journal/query1")
            .then(response => {
              vm.results2 = response.data;
            })
        },
        queryThree() {
          let vm = this;
          vm.results1 = undefined;
          vm.results2 = undefined;
          axios.get(api + "/journal/query2")
            .then(response => {
              vm.results3 = response.data;
            })
        }
      }
    }
</script>

<style scoped>

</style>
