

<template>
  <div id="app" >
    <app-overlay/>
    <!-- <thankyoualert/> -->
    <RouterView />
  </div>
</template>
  
  <script>
  import { RouterLink, RouterView } from 'vue-router';
  import thankyoualert from './thankyoualert.vue';
  import AppOverlay from './AppOverlay.vue';
  export default {
    name: 'App',
    components: {
      thankyoualert, AppOverlay
    },
    data(){
      return{
        title:"",
        currentTask:[],
        currentJob:[],
        currentUser:[]
      }
    }
  }
  </script>
  
  <style>
  body{
    background-color: #222f3e;
  }
  #app {
  
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    
  }
  </style>