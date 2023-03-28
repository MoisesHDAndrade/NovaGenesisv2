<template>
    <!-- <div>
        <div class="col-md-12 col-xs-12 col-sm-12 col-xl-12 col-lg-12 mt-5" style="padding-top:1em;padding-bottom:4rem">
            <div class="mt-3" v-if="!loading">
                <div class="list-group" >
                    <div v-for="job in jobs" :key="job.id"   class="list-group-item list-group-item-action bg-light py-3  " aria-current="true" >
                        <div class="d-flex w-100 justify-content-between align-items-center">
                            <div>
                                <h5 class="mb-1 text-dark" v-text="job.job_number"></h5>
                                <p class=" m-0  ">{{job.get_client_name}}</p>
                                <p class=" m-0 text-muted ">{{job.job_project}}</p>
                                <a :href="`https://maps.google.com/?q=${job.job_address}`" target="_blank" class="btn btn-sm btn-outline-dark px-4 text-center">
                                    <div class="d-flex align-items-center justify-content-center">
                                        <span class="bi bi-geo-alt mx-1"></span> GO
                                    </div> 
                                </a>
                            </div>
                            <span class="bi bi-arrow-right text-dark me-3 fs-3"></span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div> -->
    
    <div class="col-md-12 col-xs-12 col-sm-12 col-xl-12 col-lg-12 mt-5 " style="padding-top:1em;padding-bottom:4rem">
        <div class="d-flex justify-content-center" v-if="jobs.length <= 0">
            <div class="col-11 text-center">
                <div class="card shadow rounded-3 p-5">
                    <p class="card-title">No Jobs Registered</p>
                </div>
            </div>
        </div>
       
     <div class="row   w-100 mx-auto">
        <div class="col-md-12 col-xs-12 col-sm-12 col-xl-4 col-lg-4 my-1" v-for="job in jobs" :key="job.id">
            <div class="card shadow bg-light  rounded-3 overflow-hidden"  >
                <div class="card-body p-0 " >
                    <div class="position-relative ">
                        <div class="bg-light border-bottom " style="position: relative; display: block;width: 100%; height: 100%;z-index: 2;">
                        <!-- <div style="position: relative; display: block;width: 100%; height: 100%;background-color: rgba(255, 193, 7,0.7);z-index: 2;"> -->
                            <div style="" class="p-3 d-flex justify-content-between">
                                <div>
                                    <p class="m-0 fs-4 lead  text-dark fw-bold">{{job.job_number}}</p>
                                </div>
                                <button class="btn p-1 position-absolute top-0 end-0 " @click="getCurrentJob(job)" data-bs-toggle="offcanvas" data-bs-target="#contextJobBottomOffCanvas" aria-expanded="false">
                                    <span class="bi bi-three-dots-vertical"></span>
                                </button>
                            </div>
                        </div>
                    </div>
                    <div class="d-flex justify-content-between align-items-center px-3 py-0 mt-2">
                        <div class="col-12 me-1">
                            <div class="d-flex justify-content-between align-items-center position-relative">
                                
                                <div class="col">
                                    <!-- <p class="m-0  fw-bold fs-4">{{job.job_number}}</p> -->
                                    <p class=" m-0  ">{{job.get_client_name}}</p>
                                    <p class=" m-0 text-muted ">{{job.job_project}}</p>
                                </div>
                                <!-- <button class="btn p-1 position-absolute top-0 end-0 " @click="getCurrentJob(job)" data-bs-toggle="offcanvas" data-bs-target="#contextJobBottomOffCanvas" aria-expanded="false">
                                    <span class="bi bi-three-dots-vertical"></span>
                                </button> -->
                            </div>
                        </div>
                       
                    </div>
                    <div class="px-1 mb-2">
                        <button  class="btn btn-sm  shadow rounded-3 w-100 mt-3" style="background-color: rgba(255, 193, 7,0.4)" @click="getDetailsJob(job)">
                            <div class="d-flex align-items-center justify-content-center">
                                 Details
                            </div> 
                        </button>
                    </div>
                </div>
            </div>
        </div>
     </div>
</div>
 </template>

 <script>
    
 export default {
    
    props:['jobs'],
    data(){
        return{

        }
    },
    methods:{
        getCurrentJob(job){
            this.$emit('getJob', job)
        },
        getDetailsJob(job){
            var jobsLocalStorage;
            try{
                jobsLocalStorage = JSON.parse(localStorage.getItem("NovaGenesisApp"));
                if(jobsLocalStorage){
                    jobsLocalStorage["currentJob"] = job
                    localStorage.setItem('NovaGenesisApp', JSON.stringify(jobsLocalStorage))
                    this.$root.currentJob = job
                    console.log(this.$root.currentJob)
                }
            }
            catch(err){
                console.log('teste')
            }
            
            
            this.$router.push({name:'jobdetail', params:{id:job.id}})
        },
    }
    
}
 </script>