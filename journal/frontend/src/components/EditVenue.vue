<template>
  <div class="container is-fluid">
    <VenueForm v-if="venue !== undefined"
                    :prop_name = venue[1].name
                    :prop_state = venue[1].state
                    :prop_city = venue[1].city
                    :prop_style = venue[1].style
                    @submitVenue="editVenue"
                    @deleteVenue="removeVenue">
    </VenueForm>
  </div>
</template>

<script>
  import axios from 'axios';
  import VenueForm from './VenueForm'
  const api = "http://localhost:8000";

  export default {
    name: "EditVenue",
    data(){
      let vm = this;
      return {
        venue: undefined,
        name: vm.getVenueName(),
      }
    },
    methods: {
      editVenue(venue) {
        let vm = this;
        let index = vm.venue[0];
        let data = {
          index,
          updatedVenue: venue,
          oldVenue: vm.venue[1]
        };
        axios.put(api + '/journal/venue/update/' + vm.name, venue)
          .then(response => {
            console.log(response);
            vm.$store.commit('editVenue', data);
            vm.$router.push('/journal/concerts');
          })
          .catch(error => {
            console.log(error);
          })
      },
      removeVenue() {
        let vm = this;
        axios.delete(api + '/journal/venue/delete/' + vm.name, vm.venue[1])
          .then(response => {
            console.log(response);
            vm.$store.commit('deleteVenue', vm.venue[0]);
            vm.$router.push('/journal/concerts');
          })
          .catch(error => {
            console.log(error)
          })

      },
      getVenue(name) {
        for (let venue in this.$store.state.venues) {
          if (name === this.$store.state.venues[venue].name) {
            // Return [index, entry]
            return [venue, this.$store.state.venues[venue]];
          }
        }
        return undefined;
      },
      getVenueName() {
        let vm = this;
        return vm.$route.params.name;
      },
    },
    created () {
      let vm = this;
      if (this.$store.state.venues === null) {
        this.$store.dispatch('fetchVenues')
          .then(() =>  {
            vm.venue = vm.getVenue(vm.getVenueName());
          })
      }
      else {
        vm.venue = vm.getVenue(vm.getVenueName());
      }
    },
    components: {
      VenueForm,
    }

  }
</script>

<style scoped>

</style>

