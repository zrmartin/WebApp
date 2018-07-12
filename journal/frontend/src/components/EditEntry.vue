<template>
  <div class="container is-fluid">
    <EntryForm v-if="entry !== undefined"
                    :pub_date=getEntryDate()
                    :summary=entry[1].summary
                    :prop_first=false
                    :prop_activities=activities
                    @submitEntry="editEntry"
                    @deleteEntry="removeEntry">
    </EntryForm>
  </div>
</template>

<script>
  import axios from 'axios';
  import EntryForm from './EntryForm'
  const api = "http://localhost:8000";

  export default {
    name: "EditEntry",
    data(){
      let vm = this;
      return {
        entry: undefined,
        activities: undefined,
        date: vm.getEntryDate(),
      }
    },
    methods: {
      editEntry(entry, activities) {
        let vm = this;
        let index = vm.entry[0];
        let store_data = {
          index,
          updatedEntry: entry
        };
        axios.put(api + '/journal/entry/update/' + vm.date, entry)
          .then(response => {
            console.log(response);
            vm.$store.commit('editEntry', store_data);
            for (let activity in activities) {
              let activity_data = {
                entry: entry,
                name: activities[activity].name,
                duration: activities[activity].duration
              };
              axios.put(api + '/journal/activity/update/' + vm.activities[activity].name, activity_data)
                .then(response => {
                  console.log(response);
                  let store_activity = {
                    oldActivity: vm.activities[activity],
                    newActivity: response.data
                  };
                  vm.$store.commit('editActivity', store_activity);
                })
            }
          })
          .catch(error => {
            console.log(error);
          });
        vm.$router.push('/journal/entries');
      },
      removeEntry() {
        let vm = this;
        axios.delete(api + '/journal/entry/delete/' + vm.date, vm.entry[1])
          .then(response => {
            console.log(response);
            vm.$store.commit('deleteEntry', vm.entry[0]);
            vm.$router.push('/journal/entries');
          })
          .catch(error => {
            console.log(error)
          })

      },
      getEntry(date) {
        let d1 = new Date(date);
          for (let entry in this.$store.state.entries) {
            let d2 = new Date(this.$store.state.entries[entry].pub_date);
            if (d1.getFullYear() === d2.getFullYear() && d1.getMonth() === d2.getMonth() && d1.getUTCDate() === d2.getUTCDate()) {
              // Return [index, entry]
              return [entry, this.$store.state.entries[entry]];
            }
          }
          return undefined;
      },
      getActivities(entry) {
        let activities = [];
        let d1 = new Date(entry[1].pub_date);
        for (let activity in this.$store.state.activities) {
          let d2 = new Date(this.$store.state.activities[activity].entry.pub_date);
          if (d1.getFullYear() === d2.getFullYear() && d1.getMonth() === d2.getMonth() && d1.getUTCDate() === d2.getUTCDate()) {
            activities.push(this.$store.state.activities[activity]);
          }
        }
        return activities;
      },
      getEntryDate() {
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
      if (this.$store.state.entries === null) {
        this.$store.dispatch('fetchEntries')
          .then(() =>  {
            vm.entry = vm.getEntry(vm.getEntryDate());
            vm.activities = vm.getActivities(vm.entry);
          })
      }
      else {
        vm.entry = vm.getEntry(vm.getEntryDate());
        vm.activities = vm.getActivities(vm.entry);
      }
    },
    components: {
      EntryForm,
    }

  }
</script>

<style scoped>

</style>

