<template>
  <div class="container is-fluid">
    <EntryForm :pub_date=getCurrentDate()
               :prop_first=true
               :prop_activities=[]
               v-on:submitEntry="newEntry">
    </EntryForm>
  </div>
</template>

<script>
  import axios from 'axios';
  import EntryForm from './EntryForm'
  const api = "http://localhost:8000";

  export default {
    name: "CreateEntry",
    methods: {
      newEntry(form, activities) {
        let vm = this;
        axios.post(api + '/journal/entry/create', form)
          .then(function (response) {
            console.log(response);
            vm.$store.commit('addEntry', response.data);
            for (let activity in activities) {
              axios.post(api + '/journal/activity/create', {
                entry: form,
                name: activities[activity].name,
                duration: activities[activity].duration,
              })
                .then(function (response) {
                  vm.$store.commit('addActivity', response.data);
                })
                .catch(function (error) {
                  console.log(error);
                })
              }
            })
          .catch(function (error) {
            console.log(error);
          });
        vm.$router.push('/journal/entries');
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
      EntryForm,
    }

  }
</script>

<style scoped>

</style>

