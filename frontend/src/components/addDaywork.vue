<template>
    <div>
        <div class="modal fade" id="addDayWorkmodal" tabindex="-1" aria-labelledby="addDayWorkmodalLabel" aria-hidden="true" style="z-index:99999">
            <div class="modal-dialog modal-dialog-centered modal-fullscreen-lg-down ">
                <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title fw-light" id="addDayWorkmodalLabel">Daywork Creation Form</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form action="" method="post" id="dayworkAddForm">
                        <div class="form-group mb-2">
                            <label for="id_job_number" class="fw-light">Job</label>
                            <v-select class="rounded-3" :options="jobs"  label="job_number"  >
                                <template class="list-group" #option="{ job_number, job_project, get_client_name, id }">
                                        <li class="list-group-item" @click.prevent="getTaskJob(id)">{{ job_number}} - {{ job_project }} - {{get_client_name}}</li>
                                  </template>
                                <template class="list-group" #selected-option="{ job_number, job_project, get_client_name }">
                                        <li class="list-group-item text-truncate m-0 p-0">
                                            <span class="d-inline-block text-truncate  d-md-block d-sm-block d-lg-none" style="max-width: 250px;">
                                                {{ job_number}} - {{ job_project }} - {{get_client_name}}
                                            </span>
                                            <span class="d-inline-block text-truncate d-none d-md-none d-sm-none d-lg-block" style="max-width: 400px;">
                                                {{ job_number}} - {{ job_project }} - {{get_client_name}}
                                            </span>
                                        </li>  
                                  </template>
                            </v-select>
                        </div>
                        <div class="form-group mb-2">
                            <label class="fw-light mr-2 ">Task</label>
                            <v-select class="rounded-3" :options="tasks"  label="mjs_number"  >
                                <template class="list-group" #option="{ mjs_number, mjs_description, id}">
                                        <li class="list-group-item" @click.prevent="getTaskDescription(mjs_description, id)">{{ mjs_number}} - {{ mjs_description }} </li>
                                  </template>
                                <template class="list-group" #selected-option="{ mjs_number }">
                                        <li class="list-group-item text-truncate m-0 p-0">
                                            <span class="d-inline-block text-truncate  d-md-block d-sm-block d-lg-none" style="max-width: 250px;">
                                                {{ mjs_number}}
                                            </span>
                                            <span class="d-inline-block text-truncate d-none d-md-none d-sm-none d-lg-block" style="max-width: 400px;">
                                                {{ mjs_number}}
                                            </span>
                                        </li>  
                                  </template>
                            </v-select>
                        </div>

                        <div class="form-group mb-3">
                            <label for="id_task_description" class="fw-light">Task Description (Optional)</label>
                            <input type="text" autofocus class="form-control rounded-3" id="id_task_description"  autocomplete="off"   name="task_description" placeholder="Enter Task Description" v-model="timesheetForm.description">
                        </div>
                        <div class="form-check form-switch mb-3">
							<input class="form-check-input " type="checkbox" role="switch" id="multiple-days"  @click="checkMultipleDays($event)">
							<label class="form-check-label" for="multiple-days">Multiple days</label>
						</div>
                        <div class="d-flex justify-content-between mb-3" id="date-row">
                            <div class=" me-1" :class="multipleDays? 'col-md-6 col-sm-6 col-xs-6 col-lg-6 col-xl-6 col-6':'col-md-12 col-sm-12 col-xs-12 col-lg-12 col-xl-12 col-12 w-100'">
                              <label class="" for="id_start_date " v-text="multipleDays? 'Start Date':'Date'"></label>
                              <input type="date" required pattern="[0-9]{4}-[0-9]{2}-[0-9]{2}"   class="form-control rounded-3" id="id_start_date" name="start_date" v-model="timesheetForm.start_date">
                            </div>
                            
                            <div class="col-md-6 col-sm-6 col-xs-6 col-6   " :class="multipleDays? '':'d-none'" id="col-end-date">
                              <label class="font-weight-light " for="id_end_date">End Date</label>
                              <input type="date" required pattern="[0-9]{4}-[0-9]{2}-[0-9]{2}" class="form-control rounded-3"  id="id_end_date" name="end_date" v-model="timesheetForm.end_date">
                            </div>
                        </div>
                        <div class="row mb-3">
                            <div class="form-group col-md-6 col-sm-6 col-xs-6 col-6 ">
                                <label for="id_time_in" class="font-weight-light">Time in</label>
                                <input type="time"  class="form-control rounded-3" id="id_time_in"  name="time_in"  v-model="timesheetForm.time_in">
                            </div>
                      
                            <div class="form-group col-md-6 col-sm-6 col-xs-6 col-6 ">
                                <label for="id_time_out" class="font-weight-light">Time out</label>
                                <input type="time"  class="form-control rounded-3" id="id_time_out"  name="time_out"  v-model="timesheetForm.time_out">
                            </div>
                      
                        </div>
                        <div class="form-group form-check">
                          <input class="form-check-input" type="checkbox" id="id_break_time" @click="timesheetForm.break_time = !timesheetForm.break_time" name="break_time">
                          <label for="id_break_time" class="font-weight-light form-check-label">30 Minutes Break</label>
                        </div>
                        
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn rounded-3 px-4 btn-secondary  fw-light shadow" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn rounded-3 px-4 fw-light shadow " style="background-color: rgba(255, 193, 7,0.4);" data-bs-dismiss="modal" @click="addTimesheet">Save</button>
                </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

import axios from 'axios'
import store from '../state/index'
import moment from 'moment'

const TODAYINPUT = moment(new Date()).format('YYYY-MM-DD')
const BASE_URL = '//localhost:8000'

// const BASE_URL = 'https://e9cd-101-98-135-159.au.ngrok.io'

export default {
    
    components:{
    },
    props:[
        'jobs',
    ],
    name:'adddayworkmodal',
    data(){
        return{
            TODAY:moment(new Date()).format('YYYY-MM-DD'),
            clients:[],
            supervisors:[],
            tasks:[],
            taskDescription:"",
            task:[],
            multipleDays:false,
               	timesheetForm:{
                    start_date:TODAYINPUT,
					end_date:TODAYINPUT,
                    description:"",
                    time_in:"07:00",
                    time_out:"17:00",
                    break_time:false,
					
               }
            }
        },
    
    methods:{
        async getTaskJob(job){
            const response = await axios.get(`${BASE_URL}/api/v1/mjs/get-mjs/${job}/`, {headers:{'Authorization':`Bearer ${store.state.accessToken}`}})
            if(response.status == 200){
                this.tasks = response.data
                this.loading = false
            }
           console.log(this.tasks)
        },
        async addTimesheet(){
            this.loading = true
            const response = await axios.post(`${BASE_URL}/api/v1/timesheet/timesheet-add/`,{data:this.timesheetForm, mjs:{id:this.task}}, {headers:{'Authorization':`Bearer ${store.state.accessToken}`}})
            if(response.data.status == "success"){
                this.loading = false
                this.$root.$emit('messageToast', {"message":`Yay!You added ${response.data.rows} new ${response.data.rows > 1 ? 'rows':'row'} to your timesheet!`,"type":"success"});
            }

        },
        getTaskDescription(description, id){
            console.log(description)
            this.timesheetForm.description = description
            this.task = id
        },
        
        checkMultipleDays(event){
			if(event.target.checked){
				this.multipleDays = true
			}
			else{
				this.multipleDays =  false
				this.timesheetForm.end_date = TODAYINPUT
			}
			
		},
    },
    mounted(){
        
    },
   
}
</script>
<style>
.vs__dropdown-toggle{
    border-radius: .5em;
}
</style>