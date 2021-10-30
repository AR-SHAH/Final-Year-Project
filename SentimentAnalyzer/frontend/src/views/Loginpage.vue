<template>
  <div>
    <h1>Task 1: calling API without header</h1>
      <button v-on:click="callingWithoutheader">Click Me</button>
   
    <h2>Task 2: calling API with header set</h2>
      <button v-on:click="settingHeader">Click me</button>

      <button v-on:click="gettingToken">Get the Token</button>


        <label for="username">Enter your username</label>
        <input type="text" name="username" v-model='username'>
        <label for="username">Enter your password</label>
        <input type="text" name="password" v-model="password">
        <button v-on:click="settingDynamicHeader">Click me</button>

      <button>Click to load view</button>
    </div>
</template>

<script>

import axios from 'axios'
export default {
  name:'App',
  components: {
  },
    data(){
    return{
        username:'',
        password:'',
    }
},  
  methods: {
     callingWithoutheader:function()
            {
            axios.get('http://127.0.0.1:8000/',)
    .then(response=>{
        console.log(response.data)
  
      }).catch(err=>{
          console.log(err)
      })
 
      },


      settingHeader:function()
      {
        let url='http://127.0.0.1:8000/api/'
        let config = {
          headers:{
           'Content-Type': 'application/json'
          }
        }
        let data=JSON.stringify({"username": "shah","password": "123"})
          axios.post(url,data,config)
          .then(response=>{
            localStorage.setItem("Token","Bearer "+response.data.access)
            console.log(response.data)
            })
          .catch(err=>{console.log(err)})
   
      },
      gettingToken: function()
      {
        let url='http://127.0.0.1:8000/'
        let token = localStorage.getItem("Token")
        let config = {
         
         headers: {
            
            'Authorization':token,
            'Content-Type': 'application/json'
          }
        }
        axios.get(url,config).then(
          response=>
          {
            console.log(response.data)
          }
        ).catch(err=>(console.log(err)))

      },
      settingDynamicHeader:function()
      {
          let url='http://127.0.0.1:8000/api/'
          let config ={
            headers:{
               'Content-Type': 'application/json'
            }
          }
          let data = JSON.stringify({'username':this.username,'password':this.password})
          axios.post(url,data,config)
          .then(
            response=>
            {console.log(response.data)
            localStorage.setItem('Token','Bearer '+response.data.access)
            })
          .catch(err=>{console.log(err)})
      }
      
  },
  created()
  {
    
  }
}
</script>

<style>

</style>
