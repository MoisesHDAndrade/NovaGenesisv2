<template>
    <div>
        <loaddingSpinner v-if="loading"></loaddingSpinner>
        <top-nav-bar/>
        <sidebar/>
        <loading-card-job v-if="loading"></loading-card-job>
        
        <job-list :jobs="jobs" @getJob="setCurrentJob"></job-list>
        
        <nav-bottom @getClientSupervisor="requestClientAndSupervisorsList" ></nav-bottom>
        <job-create-modal ref="jobCreateModal" @update="getJobList"></job-create-modal>
        <job-update-modal ref="jobUpdateModal" :job="currentJob" @update="getJobList" ></job-update-modal>
        <contextBottomOffCanvas @getClientSupervisorUpdate="requestClientAndSupervisorsListUpdate" @delete-job="deleteJob"/>
        <mjs-create-modal :job="currentJob"/>
        <add-daywork :jobs="jobs"/>
    </div>
</template>
<script>
import axios from 'axios';
import store from '../../state/index';
import moment from 'moment';

import sidebar from '../../components/SideBar/sidebar.vue';
import jobList from './jobList.vue';
import jobCreateModal from './jobCreateModal.vue';
import NavBottom from './navBottom.vue';
import contextBottomOffCanvas from './contextBottomOffCanvas.vue';
import jobUpdateModal from './jobUpdateModal.vue';
import mjsCreateModal from './mjsCreateModal.vue';
import loadingCardJob from './loadingCardJob.vue';


import TopNavBar from '../../components/TopNavBar/topNavBar.vue';
import loaddingSpinner from '../../components/loaddingSpinner.vue';
import addDaywork from '../../components/addDaywork.vue';

const BASE_URL = '//localhost:8000';

export default {
  components: { 
    jobList, 
    NavBottom, 
    TopNavBar, 
    jobCreateModal,
    jobUpdateModal, 
    loaddingSpinner, 
    loadingCardJob,
    contextBottomOffCanvas,
    mjsCreateModal,
    addDaywork,
    sidebar


},

    name:'joblist',
    
    data(){
        return{
            loading:false,
            jobs:[],
            localAppStorage:[],
            currentJob:[],
            updating:false
        }
    }, 
    methods:{
        async getJobList(){
            this.loading = true;
            const response = await axios.get(`//localhost:8000/api/v1/job/joblist/`,{headers:{'Authorization':`Bearer ${store.state.accessToken}`}});
            
            if(response.status == 200){
                this.jobs = response.data;
                this.loading = false;
                this.setLocalStorage(response.data)

            }
        },
        setCurrentJob(job){
            this.currentJob = job
            var jobsLocalStorage = JSON.parse(localStorage.getItem("NovaGenesisApp"));
            jobsLocalStorage.currentJob = job
            localStorage.setItem('NovaGenesisApp', JSON.stringify(jobsLocalStorage))
        },
        setLocalStorage(res){
            var localAppStorage;
            try{
                localAppStorage =  JSON.parse(localStorage.getItem('NovaGenesisApp'))
                localAppStorage.jobs = res
                localAppStorage.lastJobUpdate = new Date()
                localStorage.setItem('NovaGenesisApp', JSON.stringify(localAppStorage));
            }
            catch(err){
                localAppStorage = {
                    jobs:res,
                    lastJobUpdate: new Date()
                };
            localStorage.setItem('NovaGenesisApp', JSON.stringify(localAppStorage));
            }
        },
        requestClientAndSupervisorsList(){
            this.$refs.jobCreateModal.getSupervisorsClientsList()
        },
        requestClientAndSupervisorsListUpdate(){
            this.$refs.jobUpdateModal.getSupervisorsClientsList()
        },
        
        verifyExistingLocalStorage(){
            try{
                var lastJobListUpdate = JSON.parse(localStorage.getItem("NovaGenesisApp"));
                this.localAppStorage = lastJobListUpdate;
                return true;
            }
            catch(err){
                this.getJobList()
                return false;
            }
        },
        getLastUpdate(){
            /*

            Get last update from list of jobs
            If last update is less than 1 hour
            Use jobs from local storage instead a query in database 
            
            */
            this.verifyExistingLocalStorage()
            var lastJobListUpdate = this.localAppStorage ? this.localAppStorage.lastJobUpdate : 0;
            console.log(lastJobListUpdate)
            var a = moment(lastJobListUpdate ? lastJobListUpdate : new Date());
            var b = moment(new Date());

            var totalMinutes = b.diff(a, 'minutes');
            if(totalMinutes > 60 || !lastJobListUpdate){
                // request job list from database
                this.getJobList()
                console.log('database query')
            }
            else{
                // get list from local storage
                this.jobs = this.localAppStorage.jobs
                console.log('local storage query')
            }
        },
        async deleteJob(){
            // this.jobs.splice(this.jobs[this.currentJob.id], 1)
            this.jobs.map(job =>{
                if(this.currentJob.id == job.id){
                    this.jobs.splice(this.jobs.indexOf(job), 1)
                }
            })
            const response = await axios.post(`${BASE_URL}/api/v1/job/job-delete/${this.currentJob.id}/`,{},  {headers:{'Authorization':`Bearer ${store.state.accessToken}`}})
            // if(response.status === 200){
            //     this.getJobList()
            // }
        },
    },
    mounted(){
        this.getJobList()
        this.getLastUpdate()
        this.$root.title = "Job List"
        document.title = "NovaGenesis | Job List"
    
    }
}
</script>