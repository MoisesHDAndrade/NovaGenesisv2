<template>
    <div class="offcanvas offcanvas-bottom bottom-offcanvas-menu" tabindex="-1" id="contextJobBottomOffCanvas" aria-labelledby="contextJobBottomOffCanvasLabel" style="height:50%">
        <div class="offcanvas-header">
            <h5 class="offcanvas-title my-0" id="contextJobBottomOffCanvasLabel"> Actions</h5>
            <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body small justify-content-center p-0" style="overflow:scroll">
            <div class="d-flex align-items-center justify-content-center w-100  ">
                <ul class="list-group w-100 text-start rounded-0" data-bs-dismiss="offcanvas">
                    <li class="list-group-item btn  text-start rounded-0 " @click.prevent="goToLocation" data-bs-dismiss="offcanvas"  >
                        <span class="bi bi-geo-alt me-2 text-muted"></span><span>Go to Location</span>
                    </li>
                    <li class="list-group-item btn  text-start rounded-0 " @click="openCreateMjsModal">
                        <span class="bi bi-plus me-2 text-muted"></span><span>Add Task / MJS</span>
                    </li>
                    <li class="list-group-item btn  text-start rounded-0 " @click="emitClientAndSupervisorsUpdate()"  aria-controls="offcanvasBottom" data-bs-dismiss="offcanvas" >
                        <span class="bi bi-pen me-2 text-muted"></span><span>Edit Job</span>
                    </li>
                    <li class="list-group-item btn  text-start rounded-0 text-danger" @click="deleteJob" >
                        <span class="bi bi-trash me-2 "></span><span>Delete Job</span>
                    </li>
                </ul>
                
            </div>
        </div>
    </div>
</template>
<script>
import Modal from 'bootstrap/js/dist/modal'
export default {
    props:[
        
    ],
    name:'contextbottomjoboffcanvas',
    methods:{
        goToLocation(){
            let href = document.createElement('a')
            href.setAttribute('href',`https://maps.google.com/?q=${this.$parent.currentJob.job_address}`)
            // href.setAttribute('href',`http://maps.apple.com/?daddr=+ ${this.$parent.currentJob.job_address} + &amp;dirflg=d&amp;t=m`)
            href.setAttribute('target','_blank')
            href.click()
            href.remove()
        },
        emitClientAndSupervisorsUpdate(){
            this.$emit('getClientSupervisorUpdate')
            this.$parent.$refs.jobUpdateModal.setJobDetail()
            this.$parent.updating = true
            var myModal = new Modal(document.getElementById('jobupdatemodal'))
            myModal.toggle()
            
        },
        openCreateMjsModal(){
            var myModal = new Modal(document.getElementById('mjscreatemodal'))
            myModal.toggle()
        },
        deleteJob(){
            this.$emit('delete-job')
        }
        
       
    }
}
</script>