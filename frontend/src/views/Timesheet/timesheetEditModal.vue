<template>
    <div>
        <div class="modal fade" id="timesheetEditModal" tabindex="-1" aria-labelledby="timesheetEditModalLabel" aria-hidden="true" style="z-index:99999">
            <div class="modal-dialog modal-dialog-centered  modal-fullscreen-lg-down">
                <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title fw-light" id="timesheetEditModalLabel">Daywork update form</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form  method="post" id="timesheetAddForm">
                        <div class="accordion accordion-flush" id="accordionFlushExample">
                            <div class="accordion-item mb-3">
                              <h2 class="accordion-header" id="flush-headingOne">
                                <button class="accordion-button collapsed shadow px-1 rounded-3 text-dark shadow-none" type="button" style="background-color: rgba(255, 193, 7,0.4);" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
                                  Details
                                </button>
                              </h2>
                              <div id="flush-collapseOne" class="accordion-collapse collapse" aria-labelledby="flush-headingOne" data-bs-parent="#accordionFlushExample">
                                <div class="accordion-body px-0">
                                    <ul class="list-group list-group-flush px-0">
                                        <li class="list-group-item">
                                            <div class="d-flex justify-content-around">
                                                <div class="col-6 text-start">
                                                    <span class="fw-bold ">Job</span>
                                                </div>
                                                <div class="col-6 text-end">
                                                    <span class="">{{daywork.get_job_number}}</span>
                                                </div>
                                            </div>
                                        </li>
                                        <li class="list-group-item">
                                            <div class="d-flex justify-content-around">
                                                <div class="col-6 text-start">
                                                    <span class="fw-bold ">Task</span>
                                                </div>
                                                <div class="col-6 text-end">
                                                    <span class="">{{daywork.get_mjs_number}}</span>
                                                </div>
                                            </div>
                                        </li>
                                        <li class="list-group-item">
                                            <div class="d-flex justify-content-around">
                                                <div class="col-6 text-start">
                                                    <span class="fw-bold ">Project</span>
                                                </div>
                                                <div class="col-6 text-end">
                                                    <span class="">{{daywork.get_project_name}}</span>
                                                </div>
                                            </div>
                                        </li>
                                        <li class="list-group-item">
                                            <div class="d-flex justify-content-around ">
                                                <div class="col-6 text-start">
                                                    <span class="fw-bold ">Client</span>
                                                </div>
                                                <div class="col-6 text-end">
                                                    <span class="">{{daywork.client}}</span>
                                                </div>
                                            </div>
                                        </li>
                                        <li class="list-group-item">
                                            <div class="d-flex justify-content-around">
                                                <div class="col-6 text-start">
                                                    <span class="fw-bold ">Supervisor</span>
                                                </div>
                                                <div class="col-6 text-end">
                                                    <span class="">{{daywork.supervisor}}</span>
                                                </div>
                                            </div>
                                        </li>
                                      </ul>
                                </div>
                              </div>
                            </div>
                           
                        </div>
                        
                        <div class="form-group ">
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
                              
                          </div>
                    
                          <div class="form-group mb-3">
                              <label for="id_description" class="font-weight-light">Description</label>
                              <input type="text"  class="form-control" id="id_description"  name="description" :placeholder="$root.currentTask.mjs_description" v-model="timesheetForm.description">
                          </div>
                    
                          <div class="form-group mb-3">
                              <label for="id_time_in" class="font-weight-light">Time in</label>
                              <input type="time"  class="form-control" id="id_time_in"  name="time_in"  v-model="timesheetForm.time_in">
                          </div>
                    
                          <div class="form-group mb-3">
                              <label for="id_time_out" class="font-weight-light">Time out</label>
                              <input type="time"  class="form-control" id="id_time_out"  name="time_out"  v-model="timesheetForm.time_out">
                          </div>
                    
                          <div class="form-group form-check">
                            <input class="form-check-input" type="checkbox" id="id_break_time" @click="timesheetForm.break_time = !timesheetForm.break_time" name="break_time" v-model="timesheetForm.break_time">
                            <label for="id_break_time" class="font-weight-light form-check-label">30 Minutes Break</label>
                          </div>
                          
                    </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn rounded-3 px-4 btn-secondary  fw-light shadow" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn rounded-3 px-4 fw-light shadow " style="background-color: rgba(255, 193, 7,0.4);" data-bs-dismiss="modal" @click="editTimesheet()">Save</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import store from '../../state/index'
import moment from 'moment'

const BASE_URL = '//localhost:8000'
const TODAYINPUT = moment(new Date()).format('YYYY-MM-DD')

export default {
    // props:[
    //     'daywork'
    // ],
    data(){
          
          return{
              multipleDays:false,
              daywork:{},
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
        getSelectedDayWork(daywork){
            console.log(daywork)
            this.daywork = daywork
            this.timesheetForm.start_date = daywork.date
            this.timesheetForm.description = daywork.description
            this.timesheetForm.time_in = daywork.time_in
            this.timesheetForm.time_out = daywork.time_out
            this.timesheetForm.break_time = daywork.break_time

        },
        async editTimesheet(){
            const response = await axios.post(`${BASE_URL}/api/v1/timesheet/timesheet-edit/${this.daywork.id}/`,
            {data:this.timesheetForm, mjs:this.mjs}, {headers:{'Authorization':`Bearer ${store.state.accessToken}`}})
            if(response.data.status == 200){
                this.$emit('update')
                this.$root.$emit('messageToast', {"message":`Day Work was updated with success`,"type":"success"})
                console.log('deu boa')
            }

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
}
</script>