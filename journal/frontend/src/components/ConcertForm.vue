<template>
  <div class="columns">
    <div class="column">
      <div class="field">
        <label class="label">Concert Date</label>
        <div class="control">
          <input class="input" type="date" v-model="date">
        </div>
        <div class="notification is-warning" v-if="errors.pub_date_invalid">
          <p><b>{{ errors.pub_date_invalid }}</b></p>
        </div>
        <div class="notification is-warning" v-if="errors.pub_date_duplicate">
          <p><b>{{ errors.pub_date_duplicate }}</b></p>
        </div>
      </div>

      <div class="field">
        <label class="label">Name</label>
        <div class="control">
          <input class="input" type="text" v-model="name">
        </div>
      </div>

      <div class="field">
        <label class="label">Venue</label>
        <div class="control">
          <input class="input" type="text" v-model="venue">
        </div>
      </div>

      <div class="field">
        <label class="label">Notes</label>
        <div class="control">
          <textarea class="textarea" placeholder="Notes about the concert" v-model="notes"></textarea>
        </div>
      </div>

      <div class="field is-grouped">
        <div class="control">
          <button class="button is-link" v-on:click="submitConcert" :disabled="!venue || !name">Submit</button>
        </div>
        <div class="control">
          <button class="button is-text"><router-link v-bind:to="'/journal/concerts'">Cancel</router-link></button>
        </div>
      </div>

      <div class="field is-grouped" v-if="prop_name">
        <div class="control">
          <button class="button is-danger" v-on:click="deleteConcert">Delete</button>
        </div>
      </div>
    </div>

    <div class="column" id ="column">

      <div class="control">
        <button class="button is-primary is-rounded is-centered" v-on:click="addFirst" v-if="first && name && venue"> + Add Artist </button>
      </div>

      <div id="addArtist" v-if="!first && name && venue" v-for="artist in artists">
        <div class="field">
          <label class="label">Artist Name</label>
          <div class="control">
            <input class="input" type="text" v-model="artist.name">
          </div>
          <label class="label">Genre</label>
          <div class="control">
            <input class="input" type="text" v-model="artist.genre">
          </div>
        </div>
        <div class="field">
          <label class="label">Rating</label>
          <div class="control">
            <div class="select">
              <select v-model="artist.rating">
                <option>0</option>
                <option>1</option>
                <option>2</option>
                <option>3</option>
                <option>4</option>
                <option>5</option>
                <option>6</option>
                <option>7</option>
                <option>8</option>
                <option>9</option>
                <option>10</option>
              </select>
            </div>
          </div>
        </div>

      </div>

      <div class="field">
        <div class="control" v-if="!first && name && venue">
          <button class="button is-primary is-rounded is-centered" v-on:click="addMultiple"> + Add Artist </button>
        </div>
      </div>
    </div>


  </div>
</template>

<script>
  export default {
    name: "ConcertForm",
    data(){
      return {
        date: this.prop_date,
        name: this.prop_name,
        venue: this.prop_venue,
        notes: this.prop_notes,
        first: this.prop_first,
        artists: this.prop_artists,
        errors: {
          pub_date_invalid: '',
          pub_date_duplicate: '',
        },
      }
    },
    methods: {
      checkDateDuplicate() {
        let vm = this;
        let d1 = new Date(vm.date);
        let d_edit = new Date(vm.prop_date);
        for (let concert in this.$store.state.concerts) {
          let d2 = new Date(this.$store.state.concerts[concert].date);
          // If the two dates match, must check if we are on create or edit page
          if (d1.getFullYear() === d2.getFullYear() && d1.getMonth() === d2.getMonth() && d1.getUTCDate() === d2.getUTCDate()) {
            // Create: Error occurs if current selected date matches any existing dates
            // Edit: Error occurs if current selected date matches any existing date besides the date of the concert we are editing
            if (!(d_edit.getFullYear() === d2.getFullYear() && d_edit.getMonth() === d2.getMonth() &&
                d_edit.getUTCDate() === d2.getUTCDate()) || vm.$route.params.day === undefined) {
                  vm.errors.pub_date_duplicate = 'Concert already exists for this date.';
                  break;
            }
          }
          else vm.errors.pub_date_duplicate = '';
        }
      },
      checkValidDate() {
        let vm = this;
        if (vm.date === '') vm.errors.pub_date_invalid = 'Invalid Date';
        else vm.errors.pub_date_invalid = '';
      },
      submitConcert() {
        let vm = this;
        vm.$emit('submitConcert', {
          date: vm.date,
          name: vm.name,
          venue: vm.venue,
          notes: vm.notes,
        }, vm.artists);
      },
      deleteConcert() {
        let vm = this;
        vm.$emit('deleteConcert', vm.date);
      },
      addFirst() {
        let vm = this;
        vm.first = false;
        vm.artists.push({ name: "", genre: "", rating: 0});
      },
      addMultiple() {
        let vm = this;
        vm.artists.push({ name: " ", genre: "", rating: 0});
      }
    },
    watch: {
      'date': function() {
        let vm = this;
        vm.checkValidDate();
        vm.checkDateDuplicate();
      }
    },
    created () {
      let vm = this;
      vm.checkDateDuplicate();
    },
    props: ['prop_date', 'prop_name', 'prop_venue', 'prop_notes', 'prop_artists', 'prop_first']
  }
</script>

<style scoped>

</style>

