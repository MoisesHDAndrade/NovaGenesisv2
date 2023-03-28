<template>
   
        <div class="col-lg-12 col-xl-12 col-md-12 col-sm-12 col-xs-12 my-2 w-100 p-0 vh-100" style="padding-top:1em">
            <!-- <div class="card shadow border-start border-4 border-top-0 border-end-0 border-bottom-0 border-primary w-100"> -->
            <div class="card shadow  w-100">
                <!-- <div class="row m-2">
                    <h5 class="card-title text-center">Jobs Locations</h5>
                </div> -->
                <div class="card-body py-0">
                    <div class="position-relative row justify-content-center">
                        <div id="map" style="width:100%;height:80vh"  ></div>
                        <div class="row justify-content-center">
                           <div class="col-md-12 col-lx-12 col-lg-12">
                            <div class="d-flex justify-content-center position-absolute align-items-center rounded-pill rounded  bg-white px-3" style="z-index:999;bottom:1em">
                                <input type="text" class="form-control border-0 shadow-none" placeholder="Search">
                                <span class="bi bi-search"></span>
                            </div>
                           </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    
</template>
<script>
export default {
    name:"cardMap",
    data(){
        return{
            lat:"",
            lon:"",
            windowHeight:0,
            windowWidth:0
        }
    },
    methods:{
        getLocation(){
                navigator.geolocation.getCurrentPosition(this.showLatitude)
            
            },
            showLatitude(position){
                this.lat = position.coords.latitude
                this.lon = position.coords.longitude
                this.getMapLocation()
            },
        getMapLocation(){
            var map = L.map(document.getElementById('map'), {
                center: [this.lat, this.lon],
                    // center: [-36.8506, 174.7679],
                    zoom: 18
                });
                var basemap = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
                }).addTo(map);
                L.marker([this.lat, this.lon]).addTo(map)
        },
        getWindowSize(){
            this.windowHeight = innerHeight
            this.windowWidth = innerWidth
        }
    },
    mounted(){
        this.getWindowSize()
        this.getLocation()
        console.log('aqui')
    }
}
</script>