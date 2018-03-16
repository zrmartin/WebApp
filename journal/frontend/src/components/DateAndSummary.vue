<template>
  <div>
    <div class="field">
      <label class="label">Entry Date</label>
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
      <label class="label">Daily Summary</label>
      <div class="control">
        <textarea class="textarea" placeholder="Enter what you did today" v-model="summ"></textarea>
      </div>
    </div>

    <div class="field is-grouped">
      <div class="control">
        <button class="button is-link" v-on:click="submitEntry">Submit</button>
      </div>
      <div class="control">
        <button class="button is-text"><router-link v-bind:to="'/journal'">Cancel</router-link></button>
      </div>
    </div>

    <div class="field is-grouped" v-if="summary">
      <div class="control">
        <button class="button is-danger" v-on:click="deleteEntry">Delete</button>
      </div>
    </div>


  </div>
</template>

<script>
  export default {
    name: "CreateEntry",
    data(){
      return {
        date: this.pub_date,
        summ: this.summary,
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
        let d_edit = new Date(vm.pub_date);
        for (let entry in this.$store.state.entries) {
          let d2 = new Date(this.$store.state.entries[entry].pub_date);
          // If the two dates match, must check if we are on create or edit page
          if (d1.getFullYear() === d2.getFullYear() && d1.getMonth() === d2.getMonth() && d1.getUTCDate() === d2.getUTCDate()) {
            // Create: Error occurs if current selected date matches any existing dates
            // Edit: Error occurs if current selected date matches any existing date besides the date of the entry we are editing
            if (!(d_edit.getFullYear() === d2.getFullYear() && d_edit.getMonth() === d2.getMonth() &&
                d_edit.getUTCDate() === d2.getUTCDate()) || vm.$route.params.day === undefined) {
                  vm.errors.pub_date_duplicate = 'Entry already exists for this date.';
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
      submitEntry() {
        let vm = this;
        vm.$emit('submitEntry', {
          pub_date: vm.date,
          summary: vm.summ});
      },
      deleteEntry() {
        let vm = this;
        vm.$emit('deleteEntry', {
          pub_date: vm.date,
          summary: vm.summ});
      },

    },
    watch: {
      'date': function() {
        let vm = this;
        vm.checkValidDate();
        vm.checkDateDuplicate();
      }
    },
    created (){
      let vm = this;
      vm.checkDateDuplicate();
    },
    props: ['pub_date', 'summary']
  }
</script>

<style scoped>

</style>

