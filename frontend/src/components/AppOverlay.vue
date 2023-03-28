<template>
    
    <div class="loading-overlay">
        <div class="row w-100 justify-content-center">
            <h1 class="text-center">NovaGenesis</h1>
            <div class="spinner-border mt-3" role="status" style="color: rgba(255, 193, 7,0.5)">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>
    </div>
</template>
<script>

export default {
    name:'appoverlay',
    data(){
        return{

        }
    },
    mounted(){
        window.onload = function () {
      setTimeout(function () {
        document.querySelector('.loading-overlay').classList.add('out');
        setTimeout(function () {
        document.querySelector('.loading-overlay').style.display="none"
      }, 1000);
      }, 2000);
      
    }
    }
}
</script>
<style>
.loading-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 99999;
  }
  .loading-overlay h1 {
    font-size: 32px;
    animation: zoomUp 7s ease-in;
  }
  .loading-overlay.out {
    animation: rollUp 1s ease-in-out;
  }
  @keyframes rollUp {
    0% {
      transform: translateY(0);
      opacity: 1;
    }
    100% {
      transform: translateY(-100%);
      opacity: 0;
    }
  }
  @keyframes zoomUp {
    0% {
      transform: scale(1);
     
    }
    100% {
      transform: scale(1.5);
      
    }
  }
</style>
