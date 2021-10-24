<template>
  <div> 
    <button class="btn btn-danger " v-on:click="compChange" id="loadButton">Click Me to load Reviews</button>
    <button class="btn btn-warning text-dark" v-on:click="compChange2">Click Me to add reviews</button>
    <component :is="comp"></component>
  </div>
</template>

<script>
import Reviews from "./Reviews.vue";
import AddReview from "./AddReview.vue";

export default {
  components: {
    reviews: Reviews,
    ar: AddReview,
  },
  data() {
    return {
      comp: "",
    };
  },
  methods: {
    compChange() {
      this.comp = "reviews";
    },
    compChange2() {
      this.comp = "ar";
    },
  },
};
</script>

<style>
</style>
