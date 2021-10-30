<template>
  <div v-if="is_authenticated">
    {{APIData[0].is_active}}
    <button v-if="!APIData[0].is_active" >Press me</button>
    </div>
</template>

<script>
import {getAPI} from '../axios-api'
export default {
  name:'App',
  components: {
  },
    data(){
    return{
        APIData:[],
        rev:'',
    }
},  


  created() {
    getAPI.get('/users',)
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
