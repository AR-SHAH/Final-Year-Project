<template>
  <div class='Reviews'>
    <h1>Add Reviews</h1>
    <form>
        <label for="review">Enter your Review: </label>
        <input type="Text" name="review" requried placeholder='Enter your review' v-model="rev"/>
        <button @click="post()">Save to DB</button>
    </form>
       
   <button @click="get()">Click here for resykts</button>
    <h1>{{myInput}}</h1>
    </div>
</template>

<script>
import axios from 'axios'
export default {
data(){
    return{
        myInput:[],
        APIData:[],
        rev:'',
    }
},

components:{
  },

methods: {
    post()
            {   const mydata=[this.rev]
                const bodyFormData = new FormData();
                bodyFormData.append('review', mydata[0]);
                axios.post("http://127.0.0.1:8000/check/",bodyFormData )
                .then(
                alert('ok')
                )
               
              
            },

     get()
     {
         
     axios.get('http://127.0.0.1:8000/check',)
    .then(response=>{
        console.log('Data Reviews')
        this.myInput = response.data
      }).catch(err=>{
          console.log(err)
      })
      },
        
        },
}
</script>

<style>
</style>
