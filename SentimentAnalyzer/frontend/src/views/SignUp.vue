<template>
  <div class="container text-danger bg-dark">
    <div class="row">
      </div>
       <div class="row">
    <div class="card"> 
     <h1 class="card-header text-center">Sign Up</h1>
    <div class="card-body">
    <form>
      <div class="row">
        <div class="col-md-2">
          <label for="firstname">Enter your First Name: </label>
        </div>
           <div class="col-md-4">
          <input type="Text" name="firstname" requried placeholder='Enter your First name' v-model="firstname"/>
           </div>
      
        <div class="col-md-2">
          <label for="review">Enter your last Name: </label>
        </div>
          <div class="col-md-4">
          <input type="Text" name="lastname" requried placeholder='Enter your Last name' v-model="lastname"/>
        </div>
     
      </div>
      <br>
      <div class="row">
           <div class="col-md-2">
          <label for="username">Enter your Username: </label>
        </div>
           <div class="col-md-4">
          <input type="Text" name="username" requried placeholder='Enter your username' v-model="username"/>
        </div>
         <div class="col-md-2">
            <label for="review">Enter your email: </label>
              </div>
              <div class="col-md-4">
            <input type="Text" name="email" requried placeholder='Enter your email' v-model="email"/>
              </div>
         
         </div>
         <br>
         <div class="row">
           
              <div class="col-md-2">
            <label for="review">Enter your password: </label>
              </div>
             <div class="col-md-4">
            <input type="password" name="password" requried placeholder='Enter your password' v-model="password"/>
          </div>

          <div class="col-md-6 text-center">
            <br>
             <button v-on:click="post" class="btn btn-primary">Sign Up</button>
          </div>
          
           
         </div>
    </form>
    </div>
  </div>
  </div>
  </div>
  
</template>

<script>
import {getAPI} from '../axios-api'
export default {
  components: {
  },
  data() {
    return {
        firstname:"",
        lastname:"",
        username:"",
        email:"",
        password:"",
    };
  },
  methods: {
       post()
            {   const mydata=[this.firstname,this.lastname,this.username,this.email,this.password]
                const bodyFormData = new FormData();
                bodyFormData.append('first_name', mydata[0]);
                bodyFormData.append('last_name', mydata[1]);
                bodyFormData.append('username', mydata[2]);
                bodyFormData.append('email', mydata[3]);
                bodyFormData.append('password', mydata[4]);
                getAPI.post("http://127.0.0.1:8000/users/",bodyFormData )
                .then(alert('Data Submitted Successfully'));
            },
},
};
</script>

<style>
</style>
