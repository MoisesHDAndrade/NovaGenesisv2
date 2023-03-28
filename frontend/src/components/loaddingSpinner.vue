<template>
    <div>
        <div class="row px-0 mx-0 " style="height:100vh; width:100%; top:0;bottom:0; left:0;right:0;z-index:99998;position:fixed; background-color: rgba(0,0,0,0.5)"  >
            <div class="d-flex justify-content-center align-items-center text-center text-white"  >
               <div>
                <div class="spinner-border " role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
               </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name:'loadingspinner'
}
</script>

