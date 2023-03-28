<template>
    <div>
        <div class="modal fade" id="jobupdatemodal" tabindex="-1" aria-labelledby="jobupdatemodalLabel" aria-hidden="true" style="z-index:99999">
            <div class="modal-dialog modal-dialog-centered modal-fullscreen-lg-down ">
                <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title fw-light" id="jobupdatemodalLabel">Job Update Form</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form action="" method="post" id="jobAddForm">
                        <div class="form-group mb-3">
                            <label for="id_job_number" class="fw-light">Job Number</label>
                            <input type="text" autofocus class="form-control" required id="id_job_number" autocomplete="off"   name="job_number" placeholder="Enter Job Number" v-model="jobForm.job">
                        </div>
                        <div class="form-group mb-3">
                            <label class="fw-light mr-2 ">Client</label>
                                <div style="">
                                    <v-select :options="clients" :filterable="true"  label="client_name"  v-model="jobForm.clientSelected"  >
                                        <template v-slot:no-options="{ search, searching }" class="text-dark">
                                            <template  v-if="searching" class="text-dark"  >
                                                    <a href="#"  @click.prevent="pushNewClient(search)">
                                                        <div class="d-flex justify-content-between mx-2">
                                                            <span class="text-black me-3">[[ search ]]</span> 
                                                            <span class="px-3 bg-yellow rounded-pill text-dark ">Create Client</span>
                                                        </div>
                                                    </a>
                                            </template>
                                        </template>
                                    </v-select>
                                </div>  
                        </div>

                        <div class="form-group mb-3">
                            <label for="id_job_project" class="fw-light">Project Name (Optional)</label>
                            <input type="text" autofocus class="form-control" id="id_job_project"  autocomplete="off"   name="job_project" placeholder="Enter Project Name" v-model="jobForm.project">
                        </div>

                        <div class="form-group mb-3">
                            <label for="id_job_address" class="fw-light" name="job_address">Site Address</label>
                            <!-- <input type="text" autofocus class="form-control" id="id_job_address"  autocomplete="off"   name="job_address" placeholder="Enter Address" v-model="jobForm.addressSelected"> -->

                            <!-- <select name="job_address" id="id_job_address" class="form-control select-form" id="id_job_address" autocomplete="off" style="width: 100%;" ></select> -->
                            <!-- <v-select label="address.properties.address_line1" :filterable="true" :options="address" @search="onSearch"> -->
                            <div class="d-flex align-items-center  justify-content-center">
                                <div class="d-flex spinner-border spinner-border-sm position-absolute  align-items-center end-0" role="status" style="margin-right:3.5rem" v-if="addressSearchLoading">
                                    <span class="visually-hidden">Loading...</span>
                                </div>
                                <v-select class="w-100" label="ad" :filterable="true" taggable :options="address" @search="debounceAddressJobCreate($event)" v-model="jobForm.addressSelected"/>
                               
                                <template slot="no-options">
                                    No address was found
                                </template>
                            </div>
                            
                        </div>

                        <div class="form-group mb-3">
                            <label class="fw-light mr-2">Supervisor</label>
                            
                            <div style="">
                                    <v-select :options="supervisors"  label="supervisor_name" :value="job.get_supervisor_name" v-model="jobForm.supervisorSelected">
                                        <template v-slot:no-options="{ search, searching }" class="text-dark">
                                                <template  v-if="searching" class="text-dark"  >
                                                    <a href="#"  @click.prevent="pushNewSupervisor(search)" class="text-decoration-none">
                                                        <div class="d-flex justify-content-between w-100 px-2">
                                                            <span class="text-black me-3">{{ search }}</span> <span class="px-2 py-0   rounded-pill text-black " style="background-color: rgba(255, 193, 7,0.4);">Create Supervisor</span>
                                                        </div>
                                                    </a>
                                                </template>
                                                <em  v-else  style="opacity: 0.5">Start typing to search for a supervisor.</em>
                                        </template>
                                    </v-select>
                            </div>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn rounded-3 px-4 btn-secondary  fw-light shadow" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn rounded-3 px-4 fw-light shadow " data-bs-dismiss="modal" style="background-color: rgba(255, 193, 7,0.4);" @click="updateJob()">Save</button>
                </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

import axios from 'axios'
import store from '../../state/index'

const BASE_URL = '//localhost:8000'
// const BASE_URL = 'https://e9cd-101-98-135-159.au.ngrok.io'

export default {
    
    components:{
    },
    props:[
    ],
    name:'jobupdatemodal',
    data(){
        return{
            clients:[],
            supervisors:[],
            address:[],
            addressSearchLoading:false,
            addressesList:[],
            addressSearchInput:"",
            counter:0,
            updating:false,
            job:[],

            jobForm:{
                clientSelected:"",
                job:"",
                project:"",
                supervisorSelected:"",
                addressSelected:"",
                }
            }
        },
    
    methods:{
        debounceAddressJobCreate(eventInput){
            if(eventInput && eventInput.length >= 4){
                this.addressSearchLoading = true
                clearTimeout(this.delayTimer)
                this.delayTimer = setTimeout(()=>{
                this.addressSearchInput = eventInput
                this.search()
            }, 500)
            }
        },

        async search(){
            this.addressesList = []
            this.address = []
            const response = await axios.get(
            `https://api.geoapify.com/v1/geocode/autocomplete?apiKey=d7deb2cf9bd94b0e87efd72fe43c8e6a&filter=countrycode:nz&bias=countrycode:nz&text=${this.addressSearchInput}`, )
            
            this.addressesList = response.data.features
            for(var item of this.addressesList){
                this.address.push({ad:`${item.properties.address_line1}, ${item.properties.suburb ? item.properties.suburb:item.properties.city}`})
            }
            this.addressSearchLoading = false
            
        },

        updateJob(){
            axios.post(`${BASE_URL}/api/v1/job/job-update/${this.job.id}/`,{data:this.jobForm},  
            {headers:{'Authorization':`Bearer ${store.state.accessToken}`}})
            .then(response=>{
                if(response.data.status == 200){
                    this.$emit('update')
                    this.$root.$emit('messageToast', {"message":`Yay! Job ${this.jobForm.job} was updated!`,"type":"success"});
                    
                }
                else{
                    // var modal = await new bootstrap.Modal(document.getElementById("jobupdatemodal")).toggle()
                    this.$root.$emit('messageToast', {"message":`${response.data.message}`,"type":"error"});
                    
                }
            })
        },

        pushNewSupervisor(sup){
            this.supervisors.push(sup)
            this.jobForm.supervisorSelected = sup
            console.log(sup)
        },

        pushNewClient(cli){
            this.clients.push(cli)
            this.jobForm.clientSelected = cli
        },

        async getClients(){
            const response = await axios.get(`${BASE_URL}/api/v1/clients/get-clients/`, {headers:{'Authorization':`Bearer ${store.state.accessToken}`}})
            this.clients = response.data
        },

        async getSupervisors(){
                const response = await axios.get(`${BASE_URL}/api/v1/supervisors/get-supervisors/`, {headers:{'Authorization':`Bearer ${store.state.accessToken}`}})
                this.supervisors = response.data
        },

        getSupervisorsClientsList(){
            this.getClients()
            this.getSupervisors()
        },
        setJobDetail(){
            this.job = this.$parent.currentJob
            this.jobForm.job = this.job.job_number
            this.jobForm.addressSelected = this.job.job_address
            this.jobForm.job_client = this.job.job_client
            this.jobForm.job_supervisor = this.job.get_supervisor_name
            this.jobForm.project = this.job.job_project
            this.jobForm.supervisorSelected = this.job.get_supervisor_name
            this.jobForm.clientSelected = this.job.get_client_name
        },
       

    },
    createOption: {
            type: Function,
            default(newOption) {
              if (typeof this.optionList[0] === 'object') {
                newOption = {[this.label]: newOption}
              }
              
              this.$emit('option:created', newOption)
              return newOption
            }
          },
}
</script>