<template>
  <div class="page-search">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="title is-size-2">Search</h2>
        <h3 class="is-size-5 has-text-grey"><strong class="has-text-grey">Search term:</strong> "<i>{{ query }}</i>" </h3>
      </div>

      <ProductBox
          v-for="product in products"
          v-bind:key="products.id"
          v-bind:product="product"
      />
    </div>
  </div>
</template>

<script>
import ProductBox from "../components/ProductBox";
import axios from "axios";

export default {
  name: "Search",
  data() {
    return{
      products: [],
      query: ''
    }
  },
  components: {
    ProductBox
  },
  mounted() {
    this.getQuery()
  },
  methods: {
    getQuery() {
      document.title = "Search | Djackets"

      let uri = window.location.search.substring(1)
      let params = new URLSearchParams(uri)

      if (params.get('query')) {
        this.query = params.get('query')
        document.title = this.query + " | Search | Djackets"
        this.performSearch()
      }
    },
    async performSearch() {
      this.$store.commit("setIsLoading", true)

      await axios
          .post(`/api/v1/products/search/`, {"query": this.query})
          .then(resp=>{
            this.products = resp.data
          })
          .catch(error=>{
            console.log(error)
            this.$root.toastErrorMessage()
          })

      this.$store.commit("setIsLoading", false)
    }
  }
}
</script>

<style scoped>

</style>