import Vue from 'vue';
import Vuex from 'Vuex';
import axios from 'axios';

Vue.use(Vuex);
const api = "http://localhost:8000";

export const store = new Vuex.Store({
  state: {
    entries: null,
    concerts: null,
    artists: null,
  },
  mutations: {
    // ***** ENTRIES ***** //
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
    },
    deleteEntry(state, entry_index) {
      state.entries.splice(entry_index, 1);
    },
    // ***** CONCERTS ***** //
    setConcerts(state, concerts) {
      state.concerts = [];
      for (let concert in concerts) {
        Vue.set(state.concerts, concert, concerts[concert]);
      }
    },
    // ****** ARTISTS ***** //
    setArtists(state, artists) {
      state.artists = [];
      for (let artist in artists) {
        Vue.set(state.artists, artist, artists[artist])
      }
    },

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
    fetchConcerts(context) {
      return new Promise((resolve, reject) => {
        axios.get(api + '/journal/concert')
          .then(response => {
            resolve(response);
            context.commit('setConcerts', response.data);
          })
          .catch(error => {
            reject(error);
            console.log(error);
          })
      })
    },
    fetchArtists(context) {
      return new Promise((resolve, reject) => {
        axios.get(api + '/journal/artist')
          .then(response => {
            resolve(response);
            context.commit('setArtists', response.data);
          })
          .catch(error => {
            reject(error);
            console.log(error);
          })
      })
    },

  },
});
