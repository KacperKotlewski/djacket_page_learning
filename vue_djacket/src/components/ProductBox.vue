<template>
  <div class="column is-3">
    <div class="box">
      <figure class="image mb-4 is-5by3">
        <img class="cover" v-bind:src="API_URL + product.get_thumbnail">
      </figure>
      <h3 class="is-size-4">{{ product.name }}</h3>
      <p class="is-size-6 has-text-grey">{{ product.price }}$</p>

      <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">View detail</router-link>

    </div>
  </div>
</template>

<script>
export default {
  name: "ProductBox",
  props: {
    product: Object
  }
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
    display: block;
    position: relative;
    overflow: hidden;
  }
  .image img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
  }
  .image img.cover {
    height: auto;
  }
</style>