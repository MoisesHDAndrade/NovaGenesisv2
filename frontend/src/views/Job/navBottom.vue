<template>
    <div>
        <nav class=" py-0 fixed-bottom bg-white border-top d-lg-none d-xl-none " style="z-index:100;font-family: 'Roboto', sans-serif">
                
            <div class="d-flex justify-content-between align-items-center ">
               
                <div class="col-4 ">
                    <button class="btn btn-white rounded py-0 my-0 text-dark shadow-none" @click="emitClientAndSupervisors()" data-bs-toggle="modal" data-bs-target="#jobcreatemodal" aria-controls="offcanvasBottom" >
                        <span class="bi bi-plus fs-5  py-0 my-0 fw-bold"></span>
                        <p class="py-0 my-0 " style="font-size:.7em;">New Job</p>
                    </button>
                </div>
                <div class="col-4 text-center">
                    <button class="btn btn-white rounded py-0 my-0 text-dark shadow-none" data-bs-toggle="modal" data-bs-target="#addDayWorkmodal" aria-controls="offcanvasBottom">
                        <span class="bi bi-calendar-plus fs-5  py-0 my-0 fw-bold text-dark"></span>
                        <p class="py-0 my-0 text-dark" style="font-size:.7em;">Daywork</p>
                    </button>
                </div>
                <div class="col-4 text-end">
                    <div class="btn-group dropup align-items-center justify-content-center mx-auto">
                        <button type="button" class="btn btn-white text-dark shadow-none" data-bs-toggle="dropdown" data-bs-target="#searchDropdown" aria-expanded="false">
                            <span class="bi bi-search  fs-5  py-0 my-0 fw-bold"></span>
                            <p class="py-0 my-0 text-dark" style="font-size:.7em;">Search</p>
                        </button>
                        <ul class="dropdown-menu py-0 mx-auto  align-items-center position-absolute justify-content-center rounded-0 border-top border-bottom border-start-0"  >
                            <div class="d-flex spinner-border spinner-border-sm position-absolute end-0 align-items-center mx-3" role="status" style="top:35%" >
                                <span class="visually-hidden">Loading...</span>
                            </div>
                            <input @input="debounce($event)" class="form-control rounded-0  py-3 justify-content-center shadow-none border-0 lh-1 mx-1" placeholder="Search a job" style="width:100vw;font-size:1.1em" >
                        </ul>
                    </div>
                </div>
            </div>
        </nav>

       
    </div>
</template>

<script>
export default {
    name:'navbottom',
    methods:{
        emitClientAndSupervisors(){
            this.$emit('getClientSupervisor')
        }
    }
}
</script>