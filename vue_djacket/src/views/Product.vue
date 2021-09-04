<template>
 <div class="page-product">
   <div class="columns is-multiline">
     <div class="column is-9">
       <figure class="image mb-6 is-5by4">
         <img class="cover" v-bind:src="product.get_image">
       </figure>

       <h1 class="title">{{product.name}}</h1>

       <p>{{product.description}}</p>
     </div>
     <div class="column is-3">
       <h2 class="subtitle">Information</h2>

       <p><strong>Price: </strong>${{product.price}}</p>

       <div class="field has-addons mt-6">
         <div class="control">
           <input type="number" class="input" min="1" v-model="quantity">
         </div>

         <div class="control">
           <a class="button is-dark" @click="addToCart">Add to cart</a>
         </div>
       </div>
     </div>
   </div>
 </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast"

export default {
  name: "Product",
  data() {
    return {
      product: {},
      quantity: 1
    }
  },
  mounted() {
    this.getProduct()
  },
  methods:{
    getProduct(){
      const category_slug = this.$route.params.category_slug
      const product_slug = this.$route.params.product_slug

      axios
          .get(`/api/v1/products/${category_slug}/${product_slug}/`, { crossdomain: true })
          .then(response=>{
            this.product = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
    addToCart() {
      if (isNaN(this.quantity) || this.quantity <1){
        this.quantity =1 
      }
      
      const item = {
        product:this.product,
        quantity: this.quantity
      }

      this.$store.commit("addToCart", item)

      toast({
        message: "The product was added to the cart",
        type: "is-success",
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: "bottom-right"
      })
    }
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
  min-height: 100%;
  height: auto;
  object-fit: cover;
}
</style>