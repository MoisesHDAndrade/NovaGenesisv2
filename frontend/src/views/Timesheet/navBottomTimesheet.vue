<template>
    <div>
        <nav class=" py-0 fixed-bottom bg-white border-top d-lg-none d-xl-none " style="z-index:100;font-family: 'Roboto', sans-serif">
                
            <div class="d-flex justify-content-center align-items-center ">
               
                
                <div class="col-4 text-center">
                    <button class="btn btn-white rounded py-0 my-0 text-dark shadow-none" data-bs-toggle="modal" data-bs-target="#addDayWorkmodal" aria-controls="offcanvasBottom">
                        <span class="bi bi-calendar-plus fs-6  py-0 my-0 fw-bold text-dark"></span>
                        <p class="py-0 my-0 text-dark" style="font-size:.7em;">Daywork</p>
                    </button>
                </div>
               
            </div>
        </nav>

       
    </div>
</template>

<script>
export default {
    name:'navbottomtimesheet',
    methods:{
       
    }
}
</script>