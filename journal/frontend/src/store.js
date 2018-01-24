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
    }
  },
  actions: {
    fetchEntries(context) {
      axios.get(api + '/journal/entry')
        .then(function(response) {
          context.commit('setEntries', response.data);
      })
      .catch(function (error) {
        console.log(error);
      })
    }
  }
});
