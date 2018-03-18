// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import moment from 'moment'
import 'bulma/css/bulma.css'
import 'font-awesome/css/font-awesome.css'

import { store } from './store'
import ListEntries from './components/ListEntries'
import CreateEntry from './components/CreateEntry'
import EditEntry from './components/EditEntry'

import ListConcerts from './components/ListConcerts'


Vue.prototype.moment = moment;
Vue.config.productionTip = false;
Vue.use(VueRouter);

const routes = [
  { path: '/journal/entries', component: ListEntries},
  { path: '/journal/entries/new', component: CreateEntry},
  { path: '/journal/entries/edit/:month/:day/:year', component: EditEntry},
  { path: '/journal/concerts', component: ListConcerts},
];

const router = new VueRouter({
  routes: routes,
  mode: 'history',
});

new Vue({
  el: '#app',
  store: store,
  router: router,
  components: { App },
  template: '<App/>'
});
