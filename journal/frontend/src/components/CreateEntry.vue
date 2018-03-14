<template>
  <div class="container is-fluid">
    <DateAndSummary v-if="$store.state.entries"
                    :pub_date=getCurrentDate()
                    v-on:submitEntry="newEntry">
    </DateAndSummary>
  </div>
</template>

<script>
  import axios from 'axios';
  import DateAndSummary from './DateAndSummary'
  const api = "http://localhost:8000";

  export default {
    name: "CreateEntry",
    methods: {
      newEntry(form) {
        let vm = this;
        axios.post(api + '/journal/entry/create', form)
          .then(function (response) {
            console.log(response);
            vm.$store.commit('addEntry', response.data);
            vm.$router.push('/journal');
          })
          .catch(function (error) {
            vm.error = true;
            vm.error_message = (error.response.request.response);
          })
      },
      getCurrentDate() {
        let vm = this;
        let today = new Date();
        let dd = today.getDate();
        let mm = today.getMonth() + 1; //January is 0!
        let yyyy = today.getFullYear();

        if(dd<10) {
            dd = '0'+dd
        }
        if(mm<10) {
            mm = '0'+mm
        }
        return (yyyy + '-' + mm + '-' + dd);
      },
    },
    created () {
      let vm = this;
      if (this.$store.state.entries === null) {
        this.$store.dispatch('fetchEntries');
      }
    },
    components: {
      DateAndSummary,
    }

  }
</script>

<style scoped>

</style>

