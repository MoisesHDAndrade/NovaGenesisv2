<template>
    <div>
        <loadding-spinner v-if="loading"></loadding-spinner>
        <div class="col-md-12 col-xs-12 col-sm-12 col-xl-12 col-lg-12 mt-5 " style="padding-top:1em;padding-bottom:4rem" >
            <top-nav-bar></top-nav-bar>
            <div class="row   w-100 mx-auto">
                <div class="col-md-12 col-xs-12 col-sm-12 col-xl-12 col-lg-12 my-1 card-user-container" v-if="loading">
                    <div class="d-flex justify-content-center">
                        <h4 class="fw-bold text-center"></h4>
                    </div>
                    <div class="card-user-info card rounded-4 shadow" >
                        <div class="card-body">
                            <div class="avatar-image-container" style="height:15em">
                                <div class="avatar-centered d-flex justify-content-center align-items-center" style="height:100%;width:auto" >
                                    <div class="col-12 text-center">
                                        <div class="image-container placeholder-glow">
                                            <div src="" alt="" class="avatar p-0 m-0 rounded-circle placeholder col-6" style="width: 8em; height: 8em;"></div>
                                        </div>
                                        <div class="container-user-name placeholder-glow">
                                            <p class="lead fw-bold m-0 placeholder">{{user_info.first_name}} {{user_info.last_name}}</p>
                                        </div>
                                        <div class="container-user-position placeholder-glow">
                                            <p class="text-muted m-0 placeholder col-8">{{user_info.position}}</p>
                                            <p class="text-muted m-0 placeholder col-8" style="font-size: 0.8rem;">{{user_info.email}}</p>
                                        </div>
                                    </div>
                                </div>
                               
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-md-12 col-xs-12 col-sm-12 col-xl-12 col-lg-12 my-1 card-user-container" v-if="!loading">
                    <div class="d-flex justify-content-center">
                        <h4 class="fw-bold text-center"></h4>
                    </div>
                    <div class="card-user-info card rounded-4 shadow" >
                        <div class="card-body">
                            <div class="avatar-image-container" style="height:15em">
                                <div class="avatar-centered d-flex justify-content-center align-items-center" style="height:100%;width:auto" >
                                    <div class="col-12 text-center">
                                        <div class="image-container">
                                            
                                            <img src="https://img.freepik.com/free-photo/portrait-white-man-isolated_53876-40306.jpg" alt="" class="avatar p-0 m-0 rounded-circle" style="width: 8em; height: 8em;">
                                        </div>
                                        <div class="container-user-name">
                                            <p class="lead fw-bold m-0">{{user_info.first_name}} {{user_info.last_name}}</p>
                                        </div>
                                        <div class="container-user-position">
                                            <p class="text-muted m-0">{{user_info.position}}</p>
                                            <p class="text-muted m-0" style="font-size: 0.8rem;">{{user_info.email}}</p>
                                        </div>
                                    </div>
                                </div>
                               
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="row   w-100 mx-auto">
                <div class="col-md-12 col-xs-12 col-sm-12 col-xl-12 col-lg-12 my-1 card-user-container mt-4">
                    <div class="d-flex justify-content-center">
                        <h4 class="fw-bold text-center">Leaves</h4>
                    </div>
                    
                    <div class="col-12">
                        <div class="card shadow rounded-4">
                            <div class="card-body">
                                <ul class="nav nav-tabs justify-content-center" id="myTab" role="tablist">
                                    <li class="nav-item" role="presentation">
                                        <button class="nav-link active" id="sickleave-tab" data-bs-toggle="tab" data-bs-target="#sickleave" type="button" role="tab" aria-controls="sickleave" aria-selected="true">Sick leaves</button>
                                    </li>
                                    <li class="nav-item" role="presentation">
                                        <button class="nav-link" id="annualleave-tab" data-bs-toggle="tab" data-bs-target="#annualleave" type="button" role="tab" aria-controls="annualleave" aria-selected="false">Annual leave</button>
                                    </li>
                                    <!-- <li class="nav-item" role="presentation">
                                        <button class="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#contact" type="button" role="tab" aria-controls="contact" aria-selected="false">Contact</button>
                                    </li> -->
                                </ul>
                                    <div class="tab-content" id="myTabContent">
                                        <div class="tab-pane fade show active" id="sickleave" role="tabpanel" aria-labelledby="sickleave-tab">
                                            <div class="col-12 mt-3 text-center">
                                                <p class="fw-bold">Remaining sick leaves</p>
                                                <p class="m-0 text-muted">7/10</p>
                                            </div>
                                            <div class="progress">
                                                <div class="progress-bar bg-success " role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" style="width:65%">
                                                </div>
                                            </div>
                                        </div>
                                        <div class="tab-pane fade" id="annualleave" role="tabpanel" aria-labelledby="annualleave-tab">
                                            <div class="col-12 mt-3 text-center">
                                                <p class="fw-bold">Remaining annual leaves</p>
                                                <p class="m-0 text-muted">12/30</p>
                                            </div>
                                            <div class="progress">
                                                <div class="progress-bar bg-success " role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" style="width:45%">
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                            </div>
                        </div>
                    </div>


                    <div class="row   w-100 mx-auto">
                        <div class="col-md-12 col-xs-12 col-sm-12 col-xl-12 col-lg-12 my-1 card-user-container mt-5">
                            <div class="d-flex justify-content-center">
                                <h4 class="fw-bold text-center">Most Worked places</h4>
                            </div>
                        </div>
                        <div class="col-12">
                            <div class="">
                                <div class="d-flex justify-content-center">
                                    <div id="map" class="p-0 m-0"></div>
                                </div>
                            </div>
                        </div>
                    </div>


                </div>
            </div>
        </div>
        <sidebar/>
    </div>
</template>
<script>
import axios from 'axios'
import store from '../../state'

import topNavBar from '../../components/TopNavBar/topNavBar.vue';
import sidebar from '../../components/SideBar/sidebar.vue';
import loaddingSpinner from '../../components/loaddingSpinner.vue';
export default {
    name:'dashboard',
    components:{
        topNavBar,
        sidebar,
        loaddingSpinner
    },
    data(){
        return{
            user_info:[],
            jobs:[],
            loading:false
        }
    },
    methods:{
        loadPageInfo(){
            this.$root.title = 'User Profile'
            document.title = "NovaGenesis | User Profile"
        },
        async loadMapLocation(){
            this.loading = true
            var map = L.map('map',{ zoomControl: true, maxZoom:15, minZoom:8 });
            for(var item of this.jobs){
                var res = await axios.get('https://nominatim.openstreetmap.org/search?format=json&limit=1&q=' + `${item.job_address}`)
                map.setView([res.data[0].lat, res.data[0].lon ],8);
                var marker = L.marker([res.data[0].lat, res.data[0].lon])
            
                marker.addTo(map)
                marker.bindPopup(`
                    <div class="text-center">
                        <p class="fw-bold m-0">${item.job_number}</p>
                        <p class="m-0 text-muted">${item.get_client_name}</p>
                        <p class="m-0 text-muted">${item.job_seconds / 3600} Hours</p>
                        
                    </div>
                `);
            }
            // map.dragging.disable();
            // map.touchZoom.disable();
            map.doubleClickZoom.disable();
            map.scrollWheelZoom.disable();
            map.boxZoom.disable();
            // map.keyboard.disable();
            L.tileLayer('https://{s}.tile.osm.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(map);
            this.loading = false
            },
            async getUserInfo(){
                this.loading = true
                const response =  await axios.get(`//localhost:8000/api/v1/accounts/get-user-info/`,{headers:{'Authorization':`Bearer ${store.state.accessToken}`}})
                if(response.status == 200){
                    this.user_info = response.data
                    this.loading = false
                }
            },
            async getWorkedHours(){
                this.loading = true
                const response =  await axios.get(`//localhost:8000/api/v1/accounts/job/performance/pwa/`,{headers:{'Authorization':`Bearer ${store.state.accessToken}`}})
                if(response.status == 200){
                    this.jobs = response.data
                    this.loading = false
                   await this.loadMapLocation()
                }
                

            }
            
    },
    mounted(){
        this.loadPageInfo()
        this.getUserInfo()
        this.getWorkedHours()
    }
    
}
</script>
<style scoped>
#map {
    position: absolute;
    width: 100%;
    height: 100%;
  }
</style>