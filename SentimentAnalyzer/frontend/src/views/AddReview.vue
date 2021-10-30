<template>
  <div class='Reviews'>
    <h1>Add Reviews</h1>
    <form>
        <select v-model="id">     
            <option v-for="(products, index) in APIData" :key="index" :value="products['product_id']">
                {{products['product_id']}}
            </option>
        </select>
        <label for="review">Enter your Review: </label>
        <input type="Text" name="review" requried placeholder='Enter your review' v-model="rev"/>
    </form>
       <button v-on:click="post">Save to DB</button>
       <h1>{{id}}</h1>

    </div>
</template>

<script>
import axios from 'axios'
import {getAPI} from '../axios-api'
export default {
data(){
    return{
        APIData:[],
        id:'',
        rev:'',
    }
},

components:{
  },

methods: {
    post()
            {   const mydata=[this.id,this.rev]
                const bodyFormData = new FormData();
                bodyFormData.append('product', mydata[0]);
                bodyFormData.append('review', mydata[1]);
                axios.post("http://127.0.0.1:8000/",bodyFormData )
                .then(response=>{
                 console.log(response.data)
                 })
                .catch(err=>{
                  console.log(err)
                  this.id = err
                 });
            },
        },  
created() {
    getAPI.get('/',)
    .then(response=>{
        console.log('Data Reviews')
        this.APIData = response.data
      }).catch(err=>{
          console.log(err)
      })
  },
}
</script>

<style>
</style>
