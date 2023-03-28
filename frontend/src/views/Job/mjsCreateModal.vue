<template>
    <div>
        <div class="modal fade rounded-3" id="mjscreatemodal" tabindex="-1" aria-labelledby="mjscreatemodalLabel" aria-hidden="true" style="z-index:99999">
            <div class="modal-dialog modal-dialog-centered modal-xl ">
                <div class="modal-content rounded-3">
                <div class="modal-header">
                    <h5 class="modal-title fw-light" id="mjscreatemodalLabel">TASK/MJS Creation<br> <span class="fw-bold">Job {{job.job_number}}</span>  </h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form action="" method="post" id="mjsAddForm">
                        <div class="form-group mb-3">
                            <label for="id_job_number" class="fw-light">MJS Number</label>
                            <input type="text" autofocus class="form-control rounded-3" required id="id_mjs_number" autocomplete="off"   name="mjs_number" placeholder="Enter Mjs Number" v-model="mjs_number">
                        </div>
                       

                        <div class="form-group mb-3">
                            <label for="id_mjs_description" class="fw-light">Description</label>
                            <input type="text" autofocus class="form-control rounded-3" id="id_mjs_description"  autocomplete="off"   name="mjs_description" placeholder="Enter Project Name" v-model="mjs_description">
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary rounded-3 fw-light shadow" data-bs-dismiss="modal" >Close</button>
                    <button type="button" class="btn rounded-3 shadow" style="background-color: rgba(255, 193, 7,0.4);" data-bs-dismiss="modal" @click="createMjs">Save</button>
                </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import store from '../../state'

const BASE_URL = '//localhost:8000'

export default {
    name:'mjscreatemodal',
    props:[
        'job'
    ],
    data(){
        return{
            mjs_number:"",
            mjs_description:"",
            
        }
    },
    methods:{
       createMjs(){
        
        axios.post(`${BASE_URL}/api/v1/mjs/mjs-create/`,{job:this.job,mjs_number:this.mjs_number, mjs_description:this.mjs_description}, {headers:{'Authorization':`Bearer ${store.state.accessToken}`}}).then(
            response=>{
                if(response.data.status == 201){
                console.log('criado')                
                }
            }
        ).catch(err=>{
            console.log(err)
        })
           
        
       },
      
       
    },
    
}
</script>