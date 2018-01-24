<template>
  <div>
    <input type="text" v-model="entry">
    <button v-on:click="newEntry"> New Entry </button>
    <br><br>
    <p v-for="entry in entries"> {{ entry }} </p>
  </div>
</template>

<script>
import axios from 'axios';

const api = "http://localhost:8000";

export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      entry: ''
    }
  },
  methods: {
    newEntry() {
      let vm = this;
      axios.post(api + '/journal/entry/create', {
        pub_date: vm.entry,
      })
        .then(function (response) {
          console.log(response)
        })
        .catch(function (error) {
          console.log(error);
        })
    }
  },
  computed: {
    entries() {
      return this.$store.state.entries;
    }
  },
  created() {
    this.$store.dispatch('fetchEntries')
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
