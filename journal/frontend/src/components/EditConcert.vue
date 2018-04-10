<template>
  <div class="container is-fluid">
    <ConcertForm v-if="$store.state.concerts && concert && artists"
                    :prop_date=getConcertDate()
                    :prop_name=concert[1].name
                    :prop_venue=concert[1].venue
                    :prop_notes=concert[1].notes
                    :prop_artists=artists
                    :prop_first = false
                    @submitConcert="editConcert"
                    @deleteConcert="removeConcert">
    </ConcertForm>
  </div>
</template>

<script>
  import axios from 'axios';
  import ConcertForm from './ConcertForm'
  const api = "http://localhost:8000";

  export default {
    name: "EditConcert",
    data(){
      let vm = this;
      return {
        concert: undefined,
        artists: undefined,
        date: vm.getConcertDate(),
      }
    },
    methods: {
      editConcert(concert) {
        let vm = this;
        let index = vm.concert[0];
        let data = {
          index,
          updatedConcert: concert
        };
        axios.put(api + '/journal/concert/update/' + vm.date, concert)
          .then(response => {
            console.log(response);
            vm.$store.commit('editConcert', data);
            vm.$router.push('/journal/concerts');
          })
          .catch(error => {
            console.log(error);
          })
      },
      removeConcert() {
        let vm = this;
        axios.delete(api + '/journal/concert/delete/' + vm.date, vm.concert[1])
          .then(response => {
            console.log(response);
            vm.$store.commit('deleteConcert', vm.concert[0]);
            vm.$router.push('/journal/concerts');
          })
          .catch(error => {
            console.log(error)
          })

      },
      getConcert(date) {
        let d1 = new Date(date);
          for (let concert in this.$store.state.concerts) {
            let d2 = new Date(this.$store.state.concerts[concert].date);
            if (d1.getFullYear() === d2.getFullYear() && d1.getMonth() === d2.getMonth() && d1.getUTCDate() === d2.getUTCDate()) {
              // Return [index, concert]
              return [concert, this.$store.state.concerts[concert]];
            }
          }
          return undefined;
      },
      getArtists(concert) {
        let vm = this;
        let artists = [];
        for (let artist in this.$store.state.artists) {
          if (this.$store.state.artists[artist].concert.date === concert[1].date) {
            artists.push(this.$store.state.artists[artist]);
          }
        }
        return artists;
      },
      getConcertDate() {
        let vm = this;
        let dd = vm.$route.params.day;
        let mm = vm.$route.params.month;
        let yyyy = vm.$route.params.year;
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
      if (this.$store.state.concerts === null) {
        this.$store.dispatch('fetchConcerts')
          .then(() => {
            vm.concert = vm.getConcert(vm.getConcertDate());
            vm.artists = vm.getArtists(vm.concert);
          });
      }
      else {
        vm.concert = vm.getConcert(vm.getConcertDate());
        vm.artists = vm.getArtists(vm.concert);
      }
    },
    components: {
      ConcertForm,
    }

  }
</script>

<style scoped>

</style>

