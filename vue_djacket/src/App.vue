<template>
<!--  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </div>-->

  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Djackets</strong></router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">

        <div class="navbar-start">
          <div class="navbar-item">

            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="what are you looking for?" name="query">
                </div>

                <div class="control">
                  <button class="button is-success">
                    <span class="icon"><i class="fas fa-search"></i></span>
                  </button>
                </div>
              </div>
            </form>

          </div>
        </div>

        <div class="navbar-end">
          <router-link to="/summer/" class="navbar-item">Summer</router-link>
          <router-link to="/winter/" class="navbar-item">Winter</router-link>

          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button is-light">Log in</router-link>
              <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i> </span>
                <span>Cart ({{ cartTotalLength }})</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading }">
      <div class="lds-dual-ring"></div>
    </div>


    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright &copy 2021</p>
    </footer>
  </div>
</template>

<script>
import {toast} from "bulma-toast";

export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: []
      },
    }
  },
  beforeCreate() {
    this.$store.commit("initializeStore")
  },
  mounted() {
    this.cart = this.$store.state.cart,
    this.API_URL
  },
  computed: {
    cartTotalLength: function() {
      let totalLength = 0;
      let items = this.cart.items
      for (let i = 0; i < items.length; i++){
        totalLength += items[i].quantity;
      }

      return totalLength;
    }
  },
  methods: {
    toastErrorMessage(){
      toast({
        message: "Something went wrong. Please Try again.",
        type: "is-danger",
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: "bottom-right"
      })
    }
  }
}
</script>

<style lang="scss">
@import "../node_modules/bulma";

html{
  overflow-y: auto;
}
#wrapper {
  display: grid;
  grid-template-rows: auto auto 1fr auto;
  min-height: 100vh;
}

/*#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}*/
.lds-dual-ring{
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after{
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
  0%{
    transform: rotate(0deg);
  }
  100%{
    transform: rotate(360deg);
  }
}

.is-loading-bar{
  height: 0;
  overflow: hidden;
  transition: all 0.3s;
  &.is-loading {
    height: 80px;
  }
}
</style>
