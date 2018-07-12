<template>
  <div class="container is-fluid">
    <VenueForm v-on:submitVenue="newVenue">
    </VenueForm>
  </div>
</template>

<script>
  import axios from 'axios';
  import VenueForm from './VenueForm'
  const api = "http://localhost:8000";

  export default {
    name: "CreateVenue",
    methods: {
      newVenue(form) {
        let vm = this;
        axios.post(api + '/journal/venue/create', form)
          .then(function (response) {
            console.log(response);
            vm.$store.commit('addVenue', response.data);
            vm.$router.push('/journal/concerts');
          })
          .catch(function (error) {
            console.log(error);
          })
      },
    },
    components: {
      VenueForm,
    }

  }
</script>

<style scoped>

</style>

