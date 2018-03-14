<template>
  <div class="container is-fluid">
    <DateAndSummary v-if="$store.state.entries"
                    :pub_date=getEntryDate()
                    :summary=getEntrySummary(getEntryDate())
                    v-on:submitEntry="editEntry">
    </DateAndSummary>
  </div>
</template>

<script>
  import axios from 'axios';
  import DateAndSummary from './DateAndSummary'
  const api = "http://localhost:8000";

  export default {
    name: "EditEntry",
    data(){
      let vm = this;
      return {
        oldDate: vm.getEntryDate(),
      }
    },
    methods: {
      editEntry(entry) {
        let vm = this;
        let index = vm.getEntry(vm.oldDate)[0];
        let data = {
          index,
          updatedEntry: entry
        };
        axios.put(api + '/journal/entry/update/' + vm.oldDate, entry)
          .then(response => {
            console.log(response);
            vm.$store.commit('editEntry', data);
            vm.$router.push('/journal');
          })
          .catch(error => {
            vm.error = true;
            vm.error_message = (error.response);
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
      getEntrySummary(date) {
        return this.getEntry(date)[1].summary;
      }
    },
    created () {
      let vm = this;
      if (this.$store.state.entries === null) {
        this.$store.dispatch('fetchEntries');
      }
    },
    components: {
      DateAndSummary,
    }

  }
</script>

<style scoped>

</style>

