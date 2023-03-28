<template>
    <div class="">
        <div class="d-flex justify-content-center " v-for="task in tasks" :key="task.id">
            <div class="list-group w-100 px-2 rounded-3 mt-2">
                <div  class="list-group-item mb-2  shadow" aria-current="true">
                  <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1 fw-bold">{{task.mjs_number}}</h5>
                    <div class="dropdown">
                        <button class="btn p-1 " role="button" id="dropdownMenuLink" data-bs-toggle="dropdown">
                            <span class="bi bi-three-dots-vertical"></span>
                        </button>
                        <ul class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                            <li>
                                <a class="dropdown-item" href="javascript:void(0)">
                                    <div class="d-flex align-items-center">
                                        <span class="bi bi-share me-2" style="font-size:.8rem"></span>
                                        <span> Share Task</span> 
                                    </div>
                                </a>
                            </li>
                            <li @click="getTask(task)">
                                <a class="dropdown-item" href="javascript:void(0)" data-bs-toggle="modal" data-bs-target="#mjsupdatemodal" >
                                    <div class="d-flex align-items-center">
                                        <span class="bi bi-pen me-2" style="font-size:.8rem"></span>
                                        <span> Edit Task</span> 
                                    </div>
                                </a>
                            </li>
                            <li @click="deleteTask(task)">
                                <a class="dropdown-item text-danger" href="javascript:void(0)">
                                    <div class="d-flex align-items-center">
                                        <span class="bi bi-trash me-2" style="font-size:.8rem"></span>
                                        <span> Delete Task</span> 
                                    </div>
                                </a>
                            </li>
                        </ul>
                    </div>
                    
                  </div>
                  <p class="mb-1">{{task.mjs_description}}</p>
                  <small><span class="fw-bold">{{task.mjs_hours}} </span> hours</small>
                  <div>
                    <button class="btn  mt-2 btn-sm w-100 rounded-3 text-black fw-boldshadow"
                    data-bs-toggle="modal" data-bs-target="#timesheetAddModal"
                    style="background-color: rgba(255, 193, 7,0.4);" 
                    @click="setCurrentTask(task)">Timesheet</button>
                  </div>
                </div>
            </div>
        </div>
        <div class="d-flex justify-content-center" v-if="tasks.length <= 0">
            <div class="col-11 text-center">
                <div class="card shadow rounded-3 p-5">
                    <p class="card-title">No Tasks Registered</p>
                </div>
            </div>
        </div>
        <mjs-update-modal @update-tasks-child="updateTasksChild"  ref="mjsupdatemodal"></mjs-update-modal>
        <timesheet-add-modal></timesheet-add-modal>
        
    </div>
</template>
<script>
import axios from 'axios';
import mjsUpdateModal from './mjsUpdateModal.vue';
import timesheetAddModal from './timesheetAddModal.vue';

export default {
    props:[
        'tasks',
    ],
    components:{
        mjsUpdateModal,
        timesheetAddModal

    },
    name:'mjslist',
    data(){
        return{
        'task':[]
           
        }
    },
    methods:{
       getTask(task){
        this.$root.currentTask = task
        this.$refs.mjsupdatemodal.setTaskDetails(task)
       },
       updateTasksChild(){
        this.$emit('update-tasks')
       },
       deleteTask(task){
        
        this.$emit('delete-task', task)
       },
       setCurrentTask(task){
        this.$root.currentTask = task
       }
    },
    mounted(){
        
    }
}
</script>