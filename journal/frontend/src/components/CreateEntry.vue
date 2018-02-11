<template>
  <div>
    <div class="container is-fluid">
        <div class="column is-half">

          <div class="field">
            <label class="label">Entry Date</label>
            <div class="control">
              <input class="input" type="date" v-model="form.pub_date">
            </div>
            <div class="notification is-warning" v-if="errors.pub_date_invalid">
              <p><b>{{ errors.pub_date_invalid }}</b></p>
            </div>
            <div class="notification is-warning" v-if="errors.pub_date_duplicate">
              <p><b>{{ errors.pub_date_duplicate }}</b></p>
            </div>
          </div>

          <div class="field">
            <label class="label">Daily Summary</label>
            <div class="control">
              <textarea class="textarea" placeholder="Enter what you did today" v-model="form.summary"></textarea>
            </div>
          </div>

          <div class="field is-grouped">
            <div class="control">
              <button class="button is-link" v-on:click="newEntry">Submit</button>
            </div>
            <div class="control">
              <button class="button is-text"><router-link v-bind:to="'/journal'">Cancel</router-link></button>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
  import axios from 'axios';
  const api = "http://localhost:8000";

  export default {
    name: "CreateEntry",
    data(){
      return {
        form: {
          pub_date: '',
          summary: '',
        },
        errors: {
          pub_date_invalid: '',
          pub_date_duplicate: '',
        },
      }
    },
    methods: {
      newEntry() {
        let vm = this;
        axios.post(api + '/journal/entry/create', vm.form)
          .then(function (response) {
            console.log(response);
            vm.$store.commit('addEntry', response.data);
            vm.$router.push('/journal');
          })
          .catch(function (error) {
            //console.log(error.response.request.response);
            vm.error = true;
            vm.error_message = (error.response.request.response);
          })
      },
      setCurrentDate() {
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
        vm.form.pub_date = (yyyy + '-' + mm + '-' + dd);
      },
      checkDateDuplicate() {
        console.log("hello");
        console.log(this.$store.state.entries);
        let vm = this;
        let d1 = new Date(vm.form.pub_date);
        for (let entry in this.$store.state.entries) {
          let d2 = new Date(this.$store.state.entries[entry].pub_date);
          if (d1.getFullYear() === d2.getFullYear() && d1.getMonth() === d2.getMonth() && d1.getUTCDate() === d2.getUTCDate()) {
            vm.errors.pub_date_duplicate = 'Entry already exists for this date.';
            break;
          }
          else vm.errors.pub_date_duplicate = '';
        }
      }
    },
    watch: {
      'form.pub_date': function() {
        let vm = this;
        if (vm.form.pub_date === '') vm.errors.pub_date_invalid = 'Invalid Date';
        else vm.errors.pub_date_invalid = '';
        vm.checkDateDuplicate();
      }
    },
    created: function() {
      let vm = this;
      vm.setCurrentDate();
      this.$store.dispatch('fetchEntries')
        .then(function(response) {
          vm.checkDateDuplicate();
        }, function(error) {
          console.log("State failed to fetch entries from database");
        });
    },
  }
</script>

<style>

</style>
