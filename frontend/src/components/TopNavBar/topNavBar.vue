<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark" id="navbar" style="z-index:99; background-color: rgba(111, 66, 193,);">
        <div class="container-fluid">
          <div class="d-flex align-items-center">
            <!-- <span class="bi bi-arrow-left text-light fs-2 me-2"></span> -->
            <a class="navbar-brand" href="javascript:void(0)" v-text="$root.title"></a>
          </div>
          <!-- bi bi-chat-left -->
         <div class="d-flex align-items-center">
          
          <RouterLink class="btn border-0 text-light p-2 border border-warning py-0" type="button" to="/message" >
            <span class="bi bi-chat-left fs-4 "></span>
          </RouterLink>
          <button class="btn border-0 text-light p-2 py-0" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasSideBar" aria-controls="offcanvasSideBar">
            <span class="bi bi-list fs-2  "></span>
          </button>
         </div>
        </div>
      </nav>
</template>
<script>
export default {
    name:'topnavbar',
    methods:{
        hideMenuOnScroll(){
            var navbar = document.getElementById("navbar")
            navbar.style.top = "0";
            var prevScrollpos = window.pageYOffset;
            window.onscroll = function() {
              var currentScrollPos = window.pageYOffset;
              if (prevScrollpos > currentScrollPos) {
                  navbar.style.top = "0";
              } else {
                  navbar.style.top = "-60px";
                
              }
              
              prevScrollpos = currentScrollPos;
              if(window.pageYOffset == 0){
                navbar.style=`top:0;`
              }
            }
        }
    },
    mounted(){
        this.hideMenuOnScroll()
    }
}
</script>

<style scoped>
#navbar {
    background-color: #333; /* Black background color */
    position: fixed; /* Make it stick/fixed */
    top: 0; /* Stay on top */
    width: 100%; /* Full width */
    transition: top 0.4s ease-in-out; /* Transition effect when sliding down (and up) */
    z-index: 999;
  }
  
  /* Style the navbar links */
 
</style>