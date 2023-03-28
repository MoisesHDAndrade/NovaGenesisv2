<template>
    <div>
        <top-nav-bar></top-nav-bar>
        <loadding-spinner v-if="loading"/>
        <div class="col-md-12 col-xs-12 col-sm-12 col-xl-12 col-lg-12 mt-5 " style="padding-top:1em;padding-bottom:4rem" >
            <div class="row   w-100 mx-auto" v-if="!loading">
               <div class="col-md-12 col-xs-12 col-sm-12 col-xl-12 col-lg-12 my-1" >
                   <div class="card shadow bg-light rounded-3 border-top-0" style="overflow:hidden;" >
                        <div class="card-body p-0 " >
                            <div class="position-relative ">
                                <div class="" style="position: relative; display: block;width: 100%; height: 100%;background-color: rgba(255, 193, 7,0.4);z-index: 2;">
                                    <div style="" class="p-3 d-flex justify-content-between">
                                        <div>
                                            <p class="m-0 fs-4 lead  text-dark fw-bold">{{job.job_number}}</p>
                                            <p class="m-0  text-muted ">{{job.job_project}}</p>
                                        </div>
                                        <span class="bi bi-three-dots-vertical"></span>
                                    </div>
                                </div>
                            </div>
                            <div class="d-flex justify-content-between align-items-center ">
                                <div class="col-12 me-1">
                                    <div class="d-flex justify-content-between align-items-center position-relative">
                                        <div class="col p-3">
                                            <p class=" m-0 fw-bold ">{{job.get_client_name}}</p>
                                            <p class=" m-0  ">{{job.get_supervisor_name}}</p>
                                            <div class="d-flex justify-content-between align-items-center">
                                                <div>
                                                    <p class=" m-0 text-muted mt-3">Total Hours</p>
                                                    <p class=" m-0 fw-bold fs-3 ">{{job.job_hours}}</p>
                                                </div>

                                                <div class="bg-light py-0 mt-3">
                                                    <button class="btn text-black shadow rounded-3 px-4 w-100  btn-sm" style="background-color: rgba(255, 193, 7,0.4);" >
                                                        <div class="d-flex align-items-center justify-content-center">
                                                            <span class="bi bi-geo-alt me-2"> </span> Location
                                                        </div> 
                                                    </button>
                                                    
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="d-flex justify-content-center w-100">
                <div class="col-md-12 mt-3 position-relative  rounded w-100 px-3" style="z-index:20; " >
                    <div class="px-3 border-bottom border-dark mb-3 w-100">
                        <p class="fw-bold text-center m-0 my-1">Tasks</p>
                    </div>
                </div>
            </div>
            <loading-card-task v-if="tasksLoading"></loading-card-task>
            <mjs-list :tasks="tasks" @update-tasks="getTasks" @delete-task="deleteTask" v-if="!tasksLoading"></mjs-list>
            <mjs-create-modal @update-tasks="getTasks"></mjs-create-modal>
            <mjs-nav-bottom></mjs-nav-bottom>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
import store from '../../state';


import topNavBar from '../../components/TopNavBar/topNavBar.vue';
import loaddingSpinner from '../../components/loaddingSpinner.vue';
import sidebar from '../../components/SideBar/sidebar.vue';

import mjsNavBottom from './mjsNavBottom.vue';
import mjsCreateModal from './mjsCreateModal.vue';
import mjsList from './mjsList.vue';
import loadingCardTask from './loadingCardTask.vue';

const BASE_URL = '//localhost:8000/api/v1'


export default {
    components:{
        topNavBar,
        loaddingSpinner,
        mjsNavBottom,
        mjsCreateModal,
        mjsList,
        loadingCardTask
    },
    name:'jobdetail',
    data(){
        return{
            job:[], 
            tasks:[],
            loading:false,
            tasksLoading:false
        }
    },
    methods:{
        getJobFromLocalStorage(){
            this.loading = true
            var job;
            try{
                job = JSON.parse(localStorage.getItem("NovaGenesisApp"))
                if(job){
                    this.job = job.currentJob
                    this.getTasks()
                    this.loading = false
                }
            }
            catch(err){
                this.getJobFromDatabase()
                this.loading = false
            }
        },
        async getJobFromDatabase(){
            const response = await axios.get(`${BASE_URL}/job/job-detail/${this.$route.params.id}/`, {headers:{'Authorization':`Bearer ${store.state.accessToken}`}})
            this.job = response.data
        },
        async getTasks(){
            this.tasksLoading = true
            this.loading = true
            console.log(this.job)
            const response = await axios.get(`${BASE_URL}/mjs/get-mjs/${this.$route.params.id}/`, {headers:{'Authorization':`Bearer ${store.state.accessToken}`}})
            if(response.status == 200){
                this.tasks = response.data
                this.tasksLoading = false
                this.loading = false
            }
        },
        createTaskOrUpdate(mjs){
            this.tasks.push(mjs)
        },
        async deleteTask(task){
            const response = await axios.post(`${BASE_URL}/mjs/mjs-delete/${task.id}/`,{},{headers:{'Authorization':`Bearer ${store.state.accessToken}`}})
            if(response.status == 200){
                this.getTasks()
            }
        }
        
    },
    mounted(){
        this.getJobFromLocalStorage()
        this.$root.title = "Job Detail"
        document.title = "NovaGenesis | Job Detail"
    }

}
</script>
<style scoped>

</style>