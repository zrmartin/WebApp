<template>
  <div class="container is-fluid">
    <ConcertForm v-on:submitConcert="newConcert"
                 :prop_date=getCurrentDate()>
    </ConcertForm>
  </div>
</template>

<script>
  import axios from 'axios';
  import ConcertForm from './ConcertForm'
  const api = "http://localhost:8000";

  export default {
    name: "CreateConcert",
    methods: {
      newConcert(concert) {
        let vm = this;
        axios.post(api + '/journal/concert/create', concert)
          .then(function (response) {
            console.log(response);
            vm.$store.commit('addConcert', response.data);
            vm.$router.push('/journal/concerts');
          })
          .catch(function (error) {
            console.log(error);
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
    created() {
      let vm = this;
      if (this.$store.state.concerts === null) {
        this.$store.dispatch('fetchConcerts');
      }
    },
    components: {
      ConcertForm,
    }
  }


</script>

<style scoped>

</style>

