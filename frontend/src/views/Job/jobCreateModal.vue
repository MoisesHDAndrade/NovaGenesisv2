<template>
    <div>
        <div class="modal fade" id="jobcreatemodal" tabindex="-1" aria-labelledby="jobcreatemodalLabel" aria-hidden="true" style="z-index:99999">
            <div class="modal-dialog modal-dialog-centered modal-fullscreen-lg-down ">
                <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title fw-light" id="jobcreatemodalLabel">Job Creation Form</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form action="" method="post" id="jobAddForm">
                        <div class="form-group mb-3">
                            <label for="id_job_number" class="fw-light">Job Number</label>
                            <input type="text" autofocus class="form-control rounded-3" required id="id_job_number" autocomplete="off"   name="job_number" placeholder="Enter Job Number" v-model="jobForm.job">
                        </div>
                        <div class="form-group mb-3">
                            <label class="fw-light mr-2 ">Client</label>
                                <span> 
                                    <!-- <a href="" data-toggle="modal" data-target="#modal2" class="btn btn-xs bg-warning"><i class="fas fa-plus"></i> New Client </a> -->
                                </span>
                                <div style="">
                                    <v-select
                                    class="rounded-3"
                                        :options="clients" 
                                        label="client_name" 
                                        v-model="jobForm.clientSelected"
                                        >
                                        <!-- <template v-slot:option="option">
                                            <span :class="">teste</span>
                                            {{ option }}
                                        </template> -->
                                        <template v-slot:no-options="{ search, searching }" class="text-dark rounded-3">
                                            <template  v-if="searching" class="text-dark"  >
                                                    <a href="#"  @click.prevent="pushNewClient(search)">
                                                        <div class="d-flex justify-content-between mx-2">
                                                            <span class="text-black me-3">{{ search }}</span> 
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
                            <input type="text" autofocus class="form-control rounded-3" id="id_job_project"  autocomplete="off"   name="job_project" placeholder="Enter Project Name" v-model="jobForm.project">
                        </div>

                        <div class="form-group mb-3">
                            <label for="id_job_address" class="fw-light" name="job_address">Site Address</label>
                            <!-- <input type="text" autofocus class="form-control rounded-3" id="id_job_address"  autocomplete="off"   name="job_address" placeholder="Enter Address" v-model="jobForm.addressSelected"> -->

                            <!-- <select name="job_address" id="id_job_address" class="form-control rounded-3 select-form" id="id_job_address" autocomplete="off" style="width: 100%;" ></select> -->
                            <!-- <v-select label="address.properties.address_line1" :filterable="true" :options="address" @search="onSearch"> -->
                            <div class="d-flex align-items-center  justify-content-center">
                                <div class="d-flex spinner-border spinner-border-sm position-absolute  align-items-center end-0" role="status" style="margin-right:3.5rem" v-if="addressSearchLoading">
                                    <span class="visually-hidden">Loading...</span>
                                </div>
                                <v-select class="w-100 rounded-3" label="ad" :filterable="true" taggable :options="address" @search="debounceAddressJobCreate($event)" v-model="jobForm.addressSelected"/>
                               
                                <template slot="no-options">
                                    No address was found
                                </template>
                            </div>
                            
                        </div>

                        <div class="form-group mb-3">
                            <label class="fw-light mr-2">Supervisor</label>
                            <span> 
                                <!-- <a href="" data-toggle="modal" data-target="#modal1" class="btn btn-xs bg-warning"><i class="fas fa-plus"></i> New Supervisor</a> -->
                            </span>
                            <div style="">
                                    <v-select class="rounded-3" :options="supervisors"  label="supervisor_name" v-model="jobForm.supervisorSelected">
                                        <template v-slot:no-options="{ search, searching }" class="text-dark">
                                                <template  v-if="searching" class="text-dark"  >
                                                    <a href="#"  @click.prevent="pushNewSupervisor(search)">
                                                        <div class="d-flex justify-content-between mx-2">
                                                            <span class="text-black me-3">{{search}}</span> 
                                                            <span class="px-3 bg-yellow rounded-pill text-dark ">Create Supervisor</span>
                                                        </div>
                                                    </a>
                                                
                                                </template>
                                                <em  v-else  style="opacity: 0.5">Start typing to search for a supervisor.</em>
                                        </template>
                                    </v-select>
                            </div>
                            <!-- <a href="" class="text-xs">Edit</a> -->
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn rounded-3 px-4 btn-secondary  fw-light shadow" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn rounded-3 px-4 fw-light shadow " style="background-color: rgba(255, 193, 7,0.4);" data-bs-dismiss="modal" @click="createJob()">Save</button>
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
    props:{
        
    },
    name:'jobcreatemodal',
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

        createJob(){
            axios.post(`${BASE_URL}/api/v1/job/create-job/`,{data:this.jobForm}, {headers:{'Authorization':`Bearer ${store.state.accessToken}`}}).then(response=>{
                if(response.data.status == 201){
                    this.$emit('update')
                    this.$root.$emit('messageToast', {"message":`Yay! Job ${this.jobForm.job} was created!`,"type":"success"});
                    
                }
                else{
                    this.$root.$emit('messageToast', {"message":`${this.jobForm.job}` ,"type":"error"});
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
            const response = await axios.get(`${BASE_URL}/api/v1/clients/get-clients/`, {headers:{'Authorization':`Bearer ${store.state.accessToken}`}} )
            this.clients = response.data
        },

        async getSupervisors(){
                const response = await axios.get(`${BASE_URL}/api/v1/supervisors/get-supervisors/`, {headers:{'Authorization':`Bearer ${store.state.accessToken}`}} )
                this.supervisors = response.data
        },

        getSupervisorsClientsList(){
            this.getClients()
            this.getSupervisors()
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
<style>
.vs__dropdown-toggle{
    border-radius: .5em;
}
</style>