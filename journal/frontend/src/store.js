import Vue from 'vue';
import Vuex from 'Vuex';
import axios from 'axios';

Vue.use(Vuex);
const api = "http://localhost:8000";

export const store = new Vuex.Store({
  state: {
    entries: [],
  },
  mutations: {
    setEntries(state, data) {
      state.entries = data;
    },
    addEntry(state, data) {
      state.entries.push(data);
    }
  },
  actions: {
    fetchEntries(context) {
      return new Promise((resolve, reject) => {
        axios.get(api + '/journal/entry')
          .then(function (response) {
            resolve(response);
            context.commit('setEntries', response.data);
          })
          .catch(function (error) {
            reject(error);
            console.log(error);
          })
      })
    }
  }
});
