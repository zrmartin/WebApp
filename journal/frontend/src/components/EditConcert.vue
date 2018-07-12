<template>
  <div class="container is-fluid">
    <ConcertForm v-if="concert !== undefined && artists !== undefined"
                    :prop_date=getConcertDate()
                    :prop_name=concert[1].name
                    :prop_venue=concert[1].venue.name
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
      // **************************************
      // TODO  ****** need to check if len(artists) > len(vm.artists). if so, need to create new artists instead of update ******
      // **************************************
      editConcert(concert, artists, venue_name) {
        let vm = this;
        let index = vm.concert[0];
        let venue = vm.getVenue(venue_name)[1];

        let api_data = {
          date: concert.date,
          name: concert.name,
          notes: concert.notes,
          venue: venue,
        };
        axios.put(api + '/journal/concert/update/' + vm.date, api_data)
          .then(response => {
            console.log(response);
            let store_data = {
              index,
              updatedConcert: response.data,
            };
            vm.$store.commit('editConcert', store_data);
            for (let artist in artists) {
              let artist_data = {
                name: artists[artist].name,
                genre: artists[artist].genre,
                rating: artists[artist].rating,
                concert: response.data,
              };
              artist_data.concert['date'] = vm.convertDate(new Date(artist_data.concert['date']));
              axios.put(api + '/journal/artist/update/' + vm.artists[artist].name, artist_data)
                .then(response => {
                  console.log(response);
                  let artists = {
                    oldArtist: vm.artists[artist],
                    newArtist: response.data
                  };
                  vm.$store.commit('editArtist', artists);
                })
            }
          })
          .catch(error => {
            console.log(error);
          })
            .catch(error => {
              console.log(error);
            });
        vm.$router.push('/journal/concerts');
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
        let artists = [];
        let d1 = new Date(concert[1].date);
        for (let artist in this.$store.state.artists) {
          let d2 = new Date(this.$store.state.artists[artist].concert.date);
          if (d1.getFullYear() === d2.getFullYear() && d1.getMonth() === d2.getMonth() && d1.getUTCDate() === d2.getUTCDate()) {
            artists.push(this.$store.state.artists[artist]);
          }
        }
        return artists;
      },
      getVenue(name) {
        let vm = this;
        for (let venue in this.$store.state.venues) {
          if(this.$store.state.venues[venue].name === name){
            // Return [index, venue]
            return [venue, this.$store.state.venues[venue]];
          }
        }
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
      convertDate(date) {
        let dd = date.getUTCDate();
        let mm = date.getMonth() + 1;
        let yyyy = date.getFullYear();
        if(dd<10) {
            dd = '0'+dd
        }
        if(mm<10) {
            mm = '0'+mm
        }
        return (yyyy + '-' + mm + '-' + dd);

      }
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

