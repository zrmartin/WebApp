<template>
    <div>
      <nav id="my-navbar-selector" class="navbar is-transparent" >
        <div class="navbar-menu">
          <div class="navbar-start">
            <!-- Journal Entry Navbar Options -->
            <div class="navbar-item has-dropdown is-hoverable">
              <a class="navbar-link">
                <router-link v-bind:to="'/journal/entries'">Journal</router-link>
              </a>
              <div class="navbar-dropdown is-boxed">
                <a class="navbar-item">
                  <router-link v-bind:to="'/journal/entries/new'">New Entry</router-link>
                </a>
              </div>
            </div>
            <!-- Concert Entry Navbar Options -->
            <div class="navbar-item has-dropdown is-hoverable">
              <a class="navbar-link">
                <router-link v-bind:to="'/journal/concerts'">Concerts</router-link>
              </a>
              <div class="navbar-dropdown is-boxed">
                <a class="navbar-item">
                  <router-link v-bind:to="'/journal/concerts/new'">New Concert</router-link>
                </a>
                <a class="navbar-item">
                  <router-link v-bind:to="'/journal/venues/new'">New Venue</router-link>
                </a>
              </div>
            </div>
            <!-- Raw Sql Query Navbar Option -->
            <div class="navbar-item">
                <router-link v-bind:to="'/journal/query'">Query</router-link>
            </div>

          </div>
          <div class="navbar-end">
            <div class="navbar-item">
                <b>Hello Zach</b>
            </div>
          </div>
        </div>
      </nav>
    </div>
</template>

<script>
    export default {
        name: "navbar"
    }
</script>

<style scoped>
#my-navbar-selector {
    z-index: 1000;
}
</style>
