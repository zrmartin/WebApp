import Vue from 'vue';
import Vuex from 'Vuex';
import axios from 'axios';

Vue.use(Vuex);
const api = "http://localhost:8000";

export const store = new Vuex.Store({
  state: {
    entries: null,
    activities: null,
    concerts: null,
    artists: null,
    venues: null,
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
      let entry = state.entries[entry_index];
      for (let activity in state.activities) {
        if (state.activities[activity].entry.date === entry.date) {
          state.activities.splice(activity, 1);
        }
      }
      state.entries.splice(entry_index, 1);
    },
    // ***** ACTIVITIES ***** //
    setActivities(state, activities) {
      state.activities = [];
      for (let activity in activities) {
        Vue.set(state.activities, activity, activities[activity]);
      }
    },
    addActivity(state, activity) {
      state.activities.push(activity);
    },
    editActivity(state, data) {
      for (let activity in state.activities) {
        if (state.activities[activity].entry.date === data.oldActivity.entry.date && state.activities[activity].name === data.oldActivity.name) {
          Vue.set(state.activities, activity, data.newActivity);
        }
      }
    },
    // ***** CONCERTS ***** //
    setConcerts(state, concerts) {
      state.concerts = [];
      for (let concert in concerts) {
        Vue.set(state.concerts, concert, concerts[concert]);
      }
    },
    addConcert(state, concert) {
      state.concerts.push(concert);
    },
    editConcert(state, data) {
      Vue.set(state.concerts, data.index, data.updatedConcert);
    },
    deleteConcert(state, concert_index) {
      let concert = state.concerts[concert_index];
      for (let artist in state.artists) {
        if (state.artists[artist].concert.date === concert.date) {
          state.artists.splice(artist, 1);
        }
      }
      state.concerts.splice(concert_index, 1);
    },
    // ****** ARTISTS ***** //
    setArtists(state, artists) {
      state.artists = [];
      for (let artist in artists) {
        Vue.set(state.artists, artist, artists[artist])
      }
    },
    addArtist(state, artist) {
      state.artists.push(artist);
    },
    editArtist(state, data) {
      for (let artist in state.artists) {
        if (state.artists[artist].name === data.oldArtist.name) {
          Vue.set(state.artists, artist, data.newArtist);
        }
      }
    },
    // ****** VENUES ***** //
    setVenues(state, venues) {
      state.venues = [];
      for (let venue in venues) {
        Vue.set(state.venues, venue, venues[venue])
      }
    },
    addVenue(state, venue) {
      state.venues.push(venue);
    },
    editVenue(state, data) {
      Vue.set(state.venues, data.index, data.updatedVenue);
      for (let concert in state.concerts) {
        if (state.concerts[concert].venue.name === data.oldVenue.name) {
          state.concerts[concert].venue = data.updatedVenue;
        }
      }
    },
    deleteVenue(state, venue_index) {
      let venue = state.venues[venue_index];
      for (let concert in state.concerts) {
        if (state.concerts[concert].venue.name === venue.name) {
          store.commit('deleteConcert', concert)
        }
      }
      state.venues.splice(venue_index, 1);
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
    fetchActivities(context) {
      return new Promise((resolve, reject) => {
        axios.get(api + '/journal/activity')
          .then(response => {
            resolve(response);
            context.commit('setActivities', response.data);
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
    fetchVenues(context) {
      return new Promise((resolve, reject) => {
        axios.get(api + '/journal/venue')
          .then(response => {
            resolve(response);
            context.commit('setVenues', response.data);
          })
          .catch(error => {
            reject(error);
            console.log(error);
          })
      })
    },

  },
});
