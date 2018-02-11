// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import 'bulma/css/bulma.css'
import 'font-awesome/css/font-awesome.css'

import { store } from './store'
import HelloWorld from './components/HelloWorld'
import CreateEntry from './components/CreateEntry'

Vue.config.productionTip = false;
Vue.use(VueRouter);

const routes = [
  { path: '/journal', component: HelloWorld},
  { path: '/journal/new', component: CreateEntry},
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
