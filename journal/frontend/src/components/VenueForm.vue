<template>
  <div>
    <div class="field">
      <label class="label">Name</label>
      <div class="control">
       <input class="input" type="text" v-model="name">
      </div>
    </div>
    <div class="field">
      <label class="label">State</label>
      <div class="control">
        <input class="input" type="text" v-model="state">
      </div>
    </div>
    <div class="field">
      <label class="label">City</label>
      <div class="control">
        <input class="input" type="text" v-model="city">
      </div>
    </div>
    <div class="field">
      <label class="label">Style</label>
      <div class="control">
        <input class="input" type="text" v-model="style">
      </div>
    </div>

    <div class="field is-grouped">
      <div class="control">
        <button class="button is-link" v-on:click="submitVenue">Submit</button>
      </div>
      <div class="control">
        <button class="button is-text"><router-link v-bind:to="'/journal/concerts'">Cancel</router-link></button>
      </div>
    </div>

    <div class="field is-grouped" v-if="prop_name">
      <div class="control">
        <button class="button is-danger" v-on:click="deleteVenue">Delete</button>
      </div>
    </div>

  </div>
</template>

<script>
  export default {
    name: "VenueForm",
    data(){
      return {
        name: this.prop_name,
        state: this.prop_state,
        city: this.prop_city,
        style: this.prop_style,
      }
    },
    methods: {
      submitVenue() {
        let vm = this;
        vm.$emit('submitVenue', {
          name: vm.name,
          state: vm.state,
          city: vm.city,
          style: vm.style});
      },
      deleteVenue() {
        let vm = this;
        vm.$emit('deleteVenue', vm.date);
      },

    },
    props: ['prop_name', 'prop_state', 'prop_city', 'prop_style']
  }
</script>

<style scoped>

</style>

