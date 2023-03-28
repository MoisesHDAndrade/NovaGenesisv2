<template>
    <div class="about">
      <topnavbar/>
      <sidebar/>
      <div class="my-5"></div>
    
      <div class="row w-100 p-0 m-0">
		    <!-- <cardMap/> -->
        <mainCards/>
		
      	<tableWorkersOnjob/>
      </div>
	 
      

    </div>
  </template>
  <script>
  import store from '../state/index'
  import sidebar from '../components/SideBar/sidebar.vue';
  import topnavbar from '../components/TopNavBar/topNavBar.vue';
  import mainCards from '../components/Dashboard/mainCards.vue';
  import tableWorkersOnjob from '../components/Dashboard/tableWorkersOnJob.vue'
  import cardMap from '../components/Dashboard/cardMap.vue';
  export default {
    components: { sidebar, topnavbar, mainCards, tableWorkersOnjob, cardMap },
    name:'about',
    data(){
      return{
		
      }
    },
    methods:{
		
    },
    mounted(){
      this.$root.title = "Dashboard"
      document.title = "Dashboard"
     
    }
  }
  </script>
  <style>
  
  </style>
  