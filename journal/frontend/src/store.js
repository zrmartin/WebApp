import Vue from 'vue';
import Vuex from 'Vuex';
import axios from 'axios';

Vue.use(Vuex);
const api = "http://localhost:8000";

export const store = new Vuex.Store({
  state: {
    entries: null,
  },
  mutations: {
    setEntries(state, entries) {
      state.entries = [];
      for (let entry in entries) {
        Vue.set(state.entries, entry, entries[entry]);
      }

    },
    addEntry(state, entry) {
      state.entries.push(entry);
    },
    editEntry(state, data) {
      Vue.set(state.entries, data.index, data.updatedEntry);
    }
  },
  actions: {
    fetchEntries(context) {
      return new Promise((resolve, reject) => {
        axios.get(api + '/journal/entry')
          .then(response => {
            resolve(response);
            context.commit('setEntries', response.data);
          })
          .catch(error => {
            reject(error);
            console.log(error);
          })
      })
    },
  },
});
