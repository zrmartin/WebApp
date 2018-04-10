<template>
  <div class="container is-fluid">
    <ConcertForm v-on:submitConcert="newConcert"
                 :prop_date=getCurrentDate()
                 :prop_artists=[]
                 :prop_first = true>
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
      newConcert(concert, artists) {
        let vm = this;
        axios.post(api + '/journal/concert/create', concert)
          .then(function (response) {
            console.log(response.data);
            vm.$store.commit('addConcert', response.data);
            for (let artist in artists) {
              axios.post(api + '/journal/artist/create', {
                name: artists[artist]['name'],
                genre: artists[artist]['genre'],
                rating: artists[artist]['rating'],
                concert: concert})
                .then(function (response) {
                  vm.$store.commit('addArtist', response.data);
                })
                .catch(function (error) {
                  console.log(error);
                })
            }
          })
          .catch(function (error) {
            console.log(error);
          });
        vm.$router.push('/journal/concerts');

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
    components: {
      ConcertForm,
    }
  }


</script>

<style scoped>

</style>

