<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#" style="margin-left: 10px;">
    <i class="fa-solid fa-piggy-bank" style="margin-right: 10px;"></i>
    Ma banque
    </a>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <router-link class="nav-link" to="/statistiques">Statistique</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/operations">Opérations</router-link>
        </li>
      </ul>
    </div>
  </nav>
  <router-view />
  <FooterGlobal class="sticky-footer"/>
</template>

<script>
import '@fortawesome/fontawesome-free/css/all.css'
import FooterGlobal from '@/components/FooterGlobal.vue'

export default {
    name: 'App',
    components: {
      FooterGlobal
    }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.sticky-footer {
  position: sticky;
  top: 100vh;
}
</style>
