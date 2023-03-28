<template>
    <div>
        <top-nav-bar></top-nav-bar>
        <sidebar></sidebar>
        <message-confirmation ref="messageConfirmation" @delete="deleteDayworks"></message-confirmation>
        <message-toast ref="messageToast"></message-toast>
        <loadding-spinner v-if="loading"></loadding-spinner>
        <timesheet-edit-modal ref="timesheeteditmodal" @update="getTimesheet"></timesheet-edit-modal>
        <div class="col-md-12 col-xs-12 col-sm-12 col-xl-12 col-lg-12 mt-5 " style="padding-top:1em;padding-bottom:4rem" v-if="!loading">
            <div class="d-flex justify-content-center px-0 mb-2"  >
                    <div class="accordion" id="searchRange">
                        <div class="accordion-item rounded-0 " style="width:100vw">
                            <h2 class="accordion-header text-center " id="headingTwo">
                                <button class="rounded-0 accordion-button collapsed shadow-none text-yellow fw-light   mx-0" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo" id="buttonCollapse">
                                    <div class="d-flex align-items-center">
                                        <span class="me-2">Filters</span> <span class="bi bi-filter"></span>
                                    </div>
                                </button>
                            </h2>
                            <div id="collapseTwo" class="accordion-collapse collapse " aria-labelledby="headingTwo" data-bs-parent="#searchRange">
                                <div class="accordion-body px-1">
                                        <div></div>
                                        <div class="card mt-3 px-0 w-100 rounded-3">
                                            <div class="card-body">
                                            <form >
                                                <div class="row ">
                                                        <div class="col-md-6 my-1 px-1 mx-0">
                                                            <label class="label">Start Date</label>
                                                            <input class="form-control " type="date" name="start_date" v-model="start_date">
                                                        </div>
                                                        <div class="col-md-6 my-1 px-1">
                                                            <label class="label">End Date</label>
                                                            <input class="form-control" type="date" name="end_date" v-model="end_date">
                                                        </div>
                                                    </div>
                                                
                                            </form>
    
                                            <div class="col-xl-4 col-lg-4 col-sm-12 col-md-12 col-xs-12">
                                                <div class="form-group mb-1" v-if="!customfilter">
                                                    <div class="form-check " id="days-off-only-div">
                                                        <input class="form-check-input"  type="checkbox" id="days_off_check" name="days_off_only"  @click="checkDaysOffOnly($event)">
                                                        <label class="form-check-label" >No worked days only</label>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col-xl-4 col-lg-4 col-sm-12 col-md-12 col-xs-12">
                                                <div class="form-group mb-1" v-if="!daysoffonly">
                                                    <div class="form-check " id="custom-filter-div">
                                                        <input class="form-check-input" type="checkbox" id="custom_filter_check" name="custom_filter_check" @click="checkCustomFilter($event)">
                                                        <label class="form-check-label" >Custom Filter</label>
                                                    </div>
                                                </div>
                                            </div>
                                            
                                            <div class="row justify-content-center w-100">
                                                <div class="form-group" id="custom-filter" v-show="customfilter">
                                                    <!-- <label class="font-weight-light" >Custom Filter</label> -->
                                                    <input class="form-control" placeholder="Search by job, mjs, client, etc" type="text" id="id_custom_filter" name="custom_filter" v-model="custom_filter_input">
                                                </div>
                                            </div>
                                            <div class="row justify-content-center mt-3">
                                                    <div class="col-md-12 col-sm-12 col-xs-12 col-lg-4 col-xl-4 text-center  px-0">
                                                        <button class="btn text-dark w-100 shadow" style="background-color: rgba(255, 193, 7,0.4);" @click="go">Go</button>
                                                    </div>
                                                </div>
                                                <div class="row justify-content-center mt-3">
                                                    <div class="col-12 text-center">
                                                        <button class="btn btn-dark shadow  py-1" v-if="searchDates" @click="getTimesheet">Clear Results</button>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                </div>
                            </div>
                        </div>
                </div>
            </div>
            <div class="d-flex justify-content-center w-100" v-if="searchDates && timesheet.length > 0"  id="send-download-pdf">
                <div class="d-flex justify-content-between my-3 align-items-center" v-if="!sending">
                    <div class="col-auto mx-1 text-end ">
                        <button class="btn btn-sm bg-warning-light    w-100" @click="sending = true"><span class="bi bi-send me-2" ></span>Send</button>
                    </div>
                    <div class="col-auto mx-1 text-start">
                        <button class="btn btn-sm  w-100 btn-outline-dark " @click="timesheetExport()"><span class="bi bi-download me-2" ></span>Download</button>
                    </div>
                </div>
                <div class="col-12 mx-1 text-center" v-if="sending">
                    <div class="col-auto mx-1 text-start">
                        <button class="btn btn-sm  w-100" @click="timesheetExport()"><span class="bi bi-download me-2" ></span>Download</button>
                    </div>
                    <div class="input-group" >
                        <input type="email" class="form-control rounded-0" :placeholder="ADDRESSEE" aria-label="Recipient's username" v-model="emailAddressee" aria-describedby="button-addon2">
                        <button class="btn btn-sm bg-warning-light rounded-0 " type="button" id="button-addon2" @click="timesheetSend()"><span class="bi bi-send me-2" ></span>Send</button>
                    </div>
                </div>
            </div>
            <div class="d-flex   w-100">
                <div class="card rounded-0 w-100">
                    <div class="card-body table-responsive-xl px-0">
                        <table class="table table-hover text-nowrap">
                            <thead class="" id="table-head">
                                <tr class="" >
                                    <th class="px-1" style="">
                                        <button class="btn py-0 px-0 m-0 d-none d-lg-block d-xl-block" v-if="selectedToDelete.length > 0">
                                            <span class="bi bi-trash-fill text-danger"></span>
                                        </button>
                                    </th>
                                    <th class="px-1 fw-light" style="">Date</th>
                                    <th class=" px-1 fw-light"  style="">Client</th>
                                    <th class=" px-1 fw-light">Address</th>
                                    <th class=" text-center px-1 fw-light">Job</th>
                                    <th class=" text-center fw-light">Task</th>
                                    <th class=" px-1 fw-light">Details</th>
                                    <th class=" px-1 fw-light">Time in</th>
                                    <th class=" px-1 fw-light">Time out</th>
                                    <th class=" px-1 fw-light">Hours on Job</th>
                                    <th class=" px-1 fw-light">Total Hours Day</th>
                                    <th class=" px-1 fw-light">Supervisor</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="obj in timesheet" :key="obj.id" class="d-table-row" :class="dayOffs.includes(obj.description) ? 'bg-grey':''">
                                    <td  class=" px-1 py-2">
                                        <input type="checkbox" name="delete" class="form-check-input check-delete" @click="selectToDelete(obj.id)" >
                                    </td>
                                    <td  class=" px-1 py-2" >
                                        <a href="#" v-if="!dayOffs.includes(obj.description)" @click.prevent="setDayWorkBeforeUpdate(obj)" data-bs-toggle="modal" data-bs-target="#timesheetEditModal"  class="text-decoration-none">{{moment(obj.date).format('DD/MM/YYYY')}}</a>
                                        <a href="#" v-else @click.prevent="setDayWorkBeforeUpdate(obj)"   class="text-decoration-none">{{moment(obj.date).format('DD/MM/YYYY')}}</a>
                                    </td>
                                    
                                    <td v-text=" obj.client" class=" px-1 py-2"></td>
                                    <td v-text="obj.address" class=" px-1 py-2"></td>
                                    <td v-text="dayOffs.includes(obj.description) ? obj.description : obj.get_job_number" class="text-center px-1 py-2"></td>
                                    <td v-text="dayOffs.includes(obj.description) ? obj.description : obj.get_mjs_number " class="text-center px-1 py-2"></td>
                                    <td v-text="obj.description" class=" px-1 py-2"></td>
                                    <td v-text="obj.time_in" class=" px-1 py-2"></td>
                                    <td v-text="obj.time_out" class=" px-1 py-2"></td>
                                    <td v-text="obj.break_time ? obj.string_getBreak : obj.string_getHoras" class=" px-1 py-2"></td>
                                    <td v-text="obj.time_out" class=" px-1 py-2"></td>
                                    <td v-text="obj.supervisor" class=" px-1 py-2"></td>
                                </tr>
                            </tbody>
                        </table>
                      
                    </div>
                </div>
            </div>
            <div class="d-flex justify-content-center my-0 " >
                <div class="col-12 text-center mt-3">
                    <button class="btn  shadow mb-5 align-items-center px-5 fw-light" v-if="hasNext && !searchDates" @click="appendTimesheet()" style="background-color: rgba(255, 193, 7,0.4);">
                        <div class="d-flex align-items-center">
                            <span v-if="buttonLoading" class="spinner-border spinner-border-sm me-2 fw-light" role="status" aria-hidden="true"></span> 
                            <span v-text="buttonLoading? 'Loading':'Load More'"></span>
                        </div>
                    </button>
                </div>
            </div>
            <div class="d-flex justify-content-center" v-if="searchDates && timesheet.length > 0">
                <div class="col-md-12 col-lg-8 col-xl-6 col-sm-12 col-xs-12 w-75">
                    <div class="card border py-1 text-center shadow rounded-4 w-100">
                        <div class="card-content py-1">
                            <div class="card-body">
                                <h5 class="card-title">Total Hours</h5>
                                <p class="card-text lead display-5" v-text="totalTime">
                                </p>
                            </div>
                        </div>
                        
                    </div>
                </div>
            </div>
            <!-- <nav-bottom-timesheet/> -->
            <nav class="py-0 fixed-bottom  border-top d-lg-none d-xl-none bg-danger " :class="selectedToDelete.length > 0 ? 'nav-delete-daywork-active': 'nav-delete-daywork-inactive'" style="z-index:100;" > 
                <div class="row justify-content-between align-items-center ">
                    <div class="col text-center">
                        <button class="btn btn-sm rounded-0 py-0 my-0 text-dark w-100 text-white" style=""  @click="preDeleteDayworks()">
                            <span class="bi bi-trash text-white fw-light py-0 my-0"></span>
                            <p class="py-0 my-0 text-white text-center" style="">Delete</p>
                        </button>
                    </div>
                </div>
            </nav>
        </div>
        <!-- <add-daywork/> -->
    </div>
</template>

<script>
import moment from 'moment';
import axios from 'axios';
import store from '../../state/index';

import topNavBar from '../../components/TopNavBar/topNavBar.vue';
import sidebar from '../../components/SideBar/sidebar.vue';
import loaddingSpinner from '../../components/loaddingSpinner.vue'
import messageConfirmation from '../../components/messageConfirmation.vue';
import messageToast from '../../components/messageToast.vue';
import timesheetEditModal from './timesheetEditModal.vue';

import navBottomTimesheet from './navBottomTimesheet.vue'
import addDaywork from '../../components/addDaywork.vue';

const BASE_URL = '//localhost:8000'
export default {
    name:'timesheetview',
    components:{
        topNavBar,
        sidebar,
        loaddingSpinner, 
        messageConfirmation,
        messageToast,
        timesheetEditModal,
        navBottomTimesheet,
        addDaywork

    },
    data(){
        return{
            TODAY:moment(new Date()).format('YYYY-MM-DD'),
            timesheet:[],
            loading:false,
            dayOffs: [
                'Sick Leave', 
                'Covid Lockdown', 
                'Public Holiday', 
                'ACC Leave', 
                'Leave Without Pay', 
                'Annual Leave', 
                'Bereavement Leave', 
                'Parental Leave', 
                'Domestic Leave'
                ],
            moment:moment,
            page:1,
            start_date:moment(new Date()).format('YYYY-MM-DD'),
            end_date:moment(new Date()).format('YYYY-MM-DD'),
            loading: true,
            searchDates:false,
            totalTime:"",
            selectedToDelete:[],
            hasNext:true,
            buttonLoading:false,
            emailAddressee:"",
            sending:false,
            selectedDayWork:{},
            customfilter:false,
            daysoffonly:false,
            custom_filter_input:"",
            
        }
    },
    methods:{
        
        async getTimesheet(){
            this.searchDates = false
            this.loading = false
            const response = await axios.get(`${BASE_URL}/api/v1/timesheet/timesheet-get/${this.page}/`, {headers:{'Authorization':`Bearer ${store.state.accessToken}`}})
            console.log(response.status)
            this.timesheet = response.data.data
            this.hasNext = response.data.hasNext
            this.loading = false
            this.sending = false
            // console.log(this.timesheet)
        },
        async appendTimesheet(){
            if(this.hasNext && !this.searchDates){
                this.buttonLoading = true
                this.page ++
                const response = await axios.get(`${BASE_URL}/api/v1/timesheet/timesheet-get/${this.page}/?format=json`, {headers:{'Authorization':`Bearer ${store.state.accessToken}`}})
                if(response.status == 401){
                    console.log('chave expirou')
                }
                this.hasNext = response.data.hasNext
                for(var item of response.data.data){
                    this.timesheet.push(item)
                }
            } 
           
            this.buttonLoading = false
           
        },
        async go(){
            
            this.searchDates = true
            
            this.customfilter = false
            // var start_date = new URL(location.href).searchParams.get('start_date')
            // var end_date = new URL(location.href).searchParams.get('end_date')
            if(!this.start_date && !this.end_date){
                this.searchDates = false
                this.$root.$emit('messageToast', {"message":`You must select the range dates`,"type":"error"});
                return
            }
            const response = await axios.get(
                `${BASE_URL}/api/v1/timesheet/timesheet-search/?start_date=${this.start_date}&end_date=${this.end_date}&custom_filter=${this.custom_filter_input}&days_off_only=${this.daysoffonly ? 'on':''}&format=json`,
                {headers:{'Authorization':`Bearer ${store.state.accessToken}`}})
            this.timesheet = response.data.data
            this.totalTime = response.data.calculatedHours
            this.loading = false
            this.closeCollapse()
            this.custom_filter_input = ""
            this.daysoffonly = false
            this.customfilter = false
            document.getElementById("days_off_check").checked = false
            document.getElementById("id_custom_filter").checked = false
        },
        checkCustomFilter(e){    
            this.customfilter = e.target.checked
        },
        checkDaysOffOnly(e){
            this.daysoffonly = e.target.checked
        },
        async preDeleteDayworks(){
            var rows = `${this.selectedToDelete.length > 1 ? 'rows':'row'}`
            this.$refs.messageConfirmation.confirmation({
                obj:this.selectedToDelete,
                typeMsg:`Do you really want delete ${this.selectedToDelete.length} ${rows}`,
                askingMsg:`You won't be able to revert this`,
                confirmedMsg:`${this.selectedToDelete.length} ${rows} was deleted with success`,
                cancelledMsg:`${this.selectedToDelete.length} ${rows} is safe :)`
            })
            // let deleted = await this.$root.$emit('messageConfirmation',  
            //     {obj:this.selectedToDelete,
            //     typeMsg:`Do you really want delete ${this.selectedToDelete.length} ${rows}`,
            //     askingMsg:`You won't be able to revert this`,
            //     confirmedMsg:`${this.selectedToDelete.length} ${rows} was deleted with success`,
            //     cancelledMsg:`${this.selectedToDelete.length} ${rows} is safe :)`});
        },
        setDayWorkBeforeUpdate(obj){
            this.$refs.timesheeteditmodal.getSelectedDayWork(obj)
        },
        deleteDayworks(){
            axios.post(`${BASE_URL}/api/v1/timesheet/timesheet-delete/`, {ts:this.selectedToDelete},{headers:{'Authorization':`Bearer ${store.state.accessToken}`}}).then(response=>{
                if (response.data.status == 200){
                    this.$refs.messageToast.toaster({"message":`${response.data.message}`,"type":"success"})

                    // se a resposta do servidor for 200
                    // percorre a lista de items a serem deletados
                    for(var item of this.selectedToDelete){
                        // mapeia os itens do timesheet
                        this.timesheet.map((e)=>{
                            // se o id dos items para ser deletados for igual ao id do timesheet
                            if(item == e.id){
                                // remove este item da lista do timesheet
                                this.timesheet.splice(this.timesheet.indexOf(e), 1)
                            }
                        })
                    }
                    // zera o array dos items a serem deletados
                    this.selectedToDelete = []
                    // percorre todos os check inputs do timesheet e desmarca todos
                    var checkDelete = document.getElementsByClassName("check-delete")
                    for(item of checkDelete){
                        item.checked = false
                    }
                }
            })
        },

        timesheetExport(){
            function update_progress(e){
                if (e.lengthComputable)
                    {
                        var percentage = Math.round((e.loaded/e.total)*100);
                        console.log("percent " + percentage + '%' );
                    }
                    else 
                    {
                        console.log("Unable to compute progress information since the total size is unknown");
                    }
                }
            // this.$root.$emit('downloadingPDFIcon')
            // this.$root.$emit('loaderFunnyMessages', '<h1>Generating your timesheet.pdf</h1>');
            var self = this
            var xhr = new XMLHttpRequest();
            xhr.open('GET', `${BASE_URL}/api/v1/timesheet/timesheet-export/?start_date=${this.start_date}&end_date=${this.end_date}`, true);
            xhr.setRequestHeader('Authorization', 'Bearer ' + store.state.accessToken);
            xhr.responseType = 'arraybuffer';
            xhr.onload = function(e) {
                e.preventDefault()
                try {
                    if (this.status == 200) {
                        
                        var blob=new Blob([this.response], {type:"application/pdf"});
                        var fileName = xhr.getResponseHeader('content-disposition').split('=')
                        var link=document.createElement('a');
                        link.href=window.URL.createObjectURL(blob);
                        link.download=fileName[1].slice(1,-1).slice(1);
                        link.click();
                        
                        const confirm = Swal.mixin({
                            customClass: {
                                confirmButton: 'btn bg-yellow m-2 shadow-none text-dark',
                                cancelButton: 'btn btn-dark shadow-none',
                                closeButton:'btn bg-warning-light  shadow-none text-dark'
                                },
                                buttonsStyling: false
                            })
                        // window.open(link.href);
                         confirm.fire({
                            icon: 'success',
                            title: 'Done!',
                            text: 'Your timesheet.pdf is ready',
                        
                            })
                            
                            // self.$root.$emit('downloadingPDFIcon')
                    
                    
                    }
                } catch (error) {
                   
                }
                
              
            };
            xhr.onloadend = function(pe) {
                console.log(pe.loaded)
              }
            xhr.send();
            
        },
     
        timesheetSend(){
            var email = this.emailAddressee ? this.emailAddressee : ADDRESSEE
            this.$root.$emit('uploadingPDFIcon')
            this.$root.$emit('loaderFunnyMessages', `<h2>Sending your timesheet.pdf<br>to ${email} </h2>`);
            this.sending = false
            var self = this
            axios.get(`${BASE_URL}/api/v1/timesheet/timesheet-send/?start_date=${this.start_date}&end_date=${this.end_date}&email=${this.emailAddressee}`).then(response =>{
                if(response.status == 200){
                    const confirm = Swal.mixin({
                        customClass: {
                            confirmButton: 'btn bg-yellow m-2 shadow-none text-dark',
                            cancelButton: 'btn btn-dark shadow-none',
                            closeButton:'btn bg-yellow  shadow-none text-dark'
                            },
                            buttonsStyling: false
                        })
                    // window.open(link.href);
                     confirm.fire({
                        icon: 'success',
                        title: 'Done!',
                        text: 'Your timesheet.pdf was sent',
                    
                        })
                        self.$root.$emit('uploadingPDFIcon')
                }
            })
        },
        closeCollapse(){
            var btn = document.getElementById("buttonCollapse")
            // if()
            btn.click()
        },

        selectToDelete(id){
            console.log(id)
            if(this.selectedToDelete.includes(id)){
                this.selectedToDelete.splice(this.selectedToDelete.indexOf(id), 1)
            }
            else{
                this.selectedToDelete.push(id)
            }
           
            
        },
        hideMenuOnScroll(){
           
            


            var navbar = document.getElementById("navbar")
            var bot = navbar.getBoundingClientRect().bottom;
            navbar.style.top = "0";
            var prevScrollpos = window.pageYOffset;
            window.onscroll = function() {
            let tableHeader = document.getElementById("table-head")
            if(tableHeader.getBoundingClientRect().top <= 0){
                tableHeader.classList.add('top-0','sticky-top','bg-white')
            }
            else{
                tableHeader.classList.remove('top-0','sticky-top')
                tableHeader.classList.style="position:relative"
            }

            let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight;


            
              var currentScrollPos = window.pageYOffset;
              if (prevScrollpos > currentScrollPos) {
                  navbar.style.top = "0";
              } else {
                  navbar.style.top = "-60px";
                
              }
              
              prevScrollpos = currentScrollPos;
              if(window.pageYOffset == 0){
                navbar.style=`top:0;`
              }
            }
        }
    },
    mounted(){
        this.getTimesheet()
        this.$root.title = "Timesheet View"
        document.title = "NovaGenesis | Timesheet View"
        this.hideMenuOnScroll()
    }
}
</script>
<style>
    .nav-delete-daywork-active{
        bottom:0;
        transition: .3s ease-in all;
    }
    .nav-delete-daywork-inactive{
        bottom:-5rem;
        transition: .5s ease-out all;
    }
    .bg-warning-light{background-color: rgba(255, 193, 7,0.4);}
</style>