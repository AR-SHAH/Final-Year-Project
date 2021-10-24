<template>
  <div class="Reviews">
    <h1>Click a product to view the comments</h1>
    <div
      v-for="(products, index) in APIData"
      :key="index"
      :value="products['product_id']"
      class="box"
    >
      <router-link
        @click.native="getId($event)"
        v-bind:id="products['product_id']"
        v-model="idd"
        :to="{ name: 'viewReview', params: { APIData: APIData, idd: idd } }"
      >
        <img
          :src="getImgUrl(products['product_id'])"
          v-bind:alt="products['product_id']"
          v-bind:id="index"
          v-on:click="getId($event)"
        />
      </router-link>
    </div>
    <viewer></viewer>
  </div>
</template>

<script>
import { getAPI } from "../axios-api";
import ViewReview from "./ViewReview.vue";
export default {
  components: {
    viewer: ViewReview,
  },

  data() {
    return {
      APIData: [],
      idd: "sdsd",
    };
  },

  methods: {
    getImgUrl(product) {
      product = product.toString();
      var images = require.context("../assets/", false, /.png$/);
      return images("./" + product + ".png");
    },
    getId(event) {
      this.idd = event.currentTarget.id;
      alert(this.idd);
    },
  },
  created() {
    getAPI
      .get("/")
      .then((response) => {
        console.log("Data Reviews");
        this.APIData = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style>
img,
.box {
  padding: 2px;
  display: inline-block;
  width: 25%;
  height: 100px;
}
</style>
