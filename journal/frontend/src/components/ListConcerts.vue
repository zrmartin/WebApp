
<template>
  <div class="container is-fluid">
    <div class="control" v-if="filterBool !== true">
      <button class="button is-primary is-centered" v-on:click="startFilter"> Filter </button>
    </div>
    <div class="field" v-if="filterBool === true">
      <div class="control">
        <label class="radio">
          <input type="radio" name="filter" v-model="filterChoice" value="Concert">
            Concert
        </label>
        <label class="radio">
          <input type="radio" name="filter" v-model="filterChoice" value="Venue">
            Venue
        </label>

        <div class="field" v-if="filterChoice === 'Concert'">
          <div class="field">
            <label class="label">Concert Name</label>
              <div class="control">
                <input class="input" type="text" v-model="concertName">
              </div>
          </div>
        </div>

        <div class="field" v-if="filterChoice === 'Venue'">
          <div class="field">
            <label class="label">Venue Name</label>
              <div class="control">
                <input class="input" type="text" v-model="venueName">
              </div>
          </div>
        </div>

        <div class="control">
          <br>
          <button class="button is-primary is-centered" v-on:click="endFilter"> Cancel </button>
        </div>
      </div>

    </div>
    <div class="columns">
      <div class="column">
        <br>
        <h1><b><u>Concerts</u></b></h1>
        <ul>
          <li v-for="concert in concerts" >
            <router-link v-bind:to="'/journal/concerts/edit/' + getDate(concert.date)">
              {{ concert.name + " - " + getDate(concert.date) }}
            </router-link>
            <ul>
              <li>
                 At {{concert.venue.name + " - " + concert.venue.city + ", " + concert.venue.state + " | " + concert.venue.style}}
              </li>
              <li>
                With Artists:
              </li>
              <li v-for="artist in artists" >
                <template v-if="getDate(concert.date) === getDate(artist.concert.date)">
                  {{ artist.name }}
                </template>
              </li>
              <br>
            </ul>
          </li>
        </ul>
      </div>
      <div class="column">
        <br>
        <h1><b><u>Venues</u></b></h1>
        <ul>
          <li v-for="venue in venues" >
            <router-link v-bind:to="'/journal/venues/edit/' + venue.name">
              {{ venue.name + " | " + venue.state + " | " + venue.city + " | " + venue.style}}
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'ListConcerts',
    data(){
      let vm = this;
      return {
        filterChoice: undefined,
        filterBool: false,
        concertName: undefined,
        venueName: undefined,
      }
    },
    methods: {
      getDate (pub_date) {
        let date = new Date(pub_date);
        let month = date.getMonth() + 1;
        let day = date.getUTCDate();
        let year = date.getFullYear();
        return month + "/" + day + "/" + year;
      },
      startFilter(){
        let vm = this;
        vm.filterBool = true;
      },
      endFilter() {
        let vm = this;
        vm.filterChoice = undefined;
        vm.concertName = undefined;
        vm.venueName = undefined;
        vm.filterBool = false;
      }
    },
    computed: {
      concerts() {
        let vm = this;
        let concerts = [];
        if (vm.concertName === undefined) {
          return this.$store.state.concerts;
        }
        else {
          for (let concert in this.$store.state.concerts) {
            if (this.$store.state.concerts[concert].name.toLowerCase().includes(vm.concertName.toLowerCase())) {
              concerts.push(this.$store.state.concerts[concert]);
            }
          }
          return concerts;
        }
      },
      artists() {
        return this.$store.state.artists;
      },
      venues() {
        let vm = this;
        let venues = [];
        if (vm.venueName === undefined) {
          return this.$store.state.venues;
        }
        else {
          for (let venue in this.$store.state.venues) {
            if (this.$store.state.venues[venue].name.toLowerCase().includes(vm.venueName.toLowerCase())) {
              venues.push(this.$store.state.venues[venue]);
            }
          }
          return venues;
        }
      }
    },
}
</script>

<style scoped>

</style>

