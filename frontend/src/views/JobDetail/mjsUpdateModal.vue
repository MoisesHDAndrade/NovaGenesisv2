<template>
    <div>
        <div class="modal fade" id="mjsupdatemodal" tabindex="-1" aria-labelledby="mjsupdatemodalLabel" aria-hidden="true" style="z-index:99999">
            <div class="modal-dialog modal-dialog-centered modal-xl">
                <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title fw-light" id="mjsupdatemodalLabel">Task Update Form</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form action="" method="post" id="mjsAddForm">
                        <div class="form-group mb-3">
                            <label for="id_job_number" class="fw-light">Task</label>
                            <input type="text" autofocus class="form-control" required id="id_mjs_number" autocomplete="off"   name="mjs_number" placeholder="Enter Task Number" v-model="mjs_number">
                        </div>
                       

                        <div class="form-group mb-3">
                            <label for="id_mjs_description" class="fw-light">Description</label>
                            <input type="text" autofocus class="form-control" id="id_mjs_description"  autocomplete="off"   name="mjs_description" placeholder="Enter Description" v-model="mjs_description">
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn rounded-3 px-4 btn-secondary  fw-light shadow" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn rounded-3 px-4 fw-light shadow " data-bs-dismiss="modal" @click="updateMjs()" style="background-color: rgba(255, 193, 7,0.4);">Save</button>
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
            mjs_number:"",
            mjs_description:"",
            task:[],

            }
        },
    
    methods:{
        
        updateMjs(){
            axios.post(`${BASE_URL}/api/v1/mjs/mjs-update/${this.task.id}/`,{mjs_number:this.mjs_number, mjs_description:this.mjs_description}, {headers:{'Authorization':`Bearer ${store.state.accessToken}`}})
            .then(response=>{
                if(response.status == 200){
                    this.$emit('update-tasks-child')
                }
            })
        },
        setTaskDetails(task){
            this.mjs_number = task.mjs_number
            this.mjs_description = task.mjs_description
            this.task = task
        }

       
       

    },
    mounted(){
    }
}
</script>
