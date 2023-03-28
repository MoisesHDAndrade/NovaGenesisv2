<template>
    <div>
        <top-nav-bar/>
        <sidebar/>
        <div class="col-md-12 col-xs-12 col-sm-12 col-xl-12 col-lg-12 mt-5 " style="padding-top:1em;padding-bottom:4rem">
            <div class="row w-100 mx-auto ">
                <ul class="nav nav-tabs justify-content-center " id="myTab" role="tablist">
                    <li class="nav-item" role="presentation">
                      <button class="nav-link active" id="basic-tab" data-bs-toggle="tab" data-bs-target="#basic" type="button" role="tab" aria-controls="basic" aria-selected="true">Basic</button>
                    </li>
                    <li class="nav-item" role="presentation">
                      <button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile" type="button" role="tab" aria-controls="profile" aria-selected="false">Profile</button>
                    </li>
                    <li class="nav-item" role="presentation">
                      <button class="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#contact" type="button" role="tab" aria-controls="contact" aria-selected="false">Contact</button>
                    </li>
                  </ul>
                  <div class="tab-content bg-white mx-0 pb-5" id="myTabContent">
                    <div class="tab-pane fade show active" id="basic" role="tabpanel" aria-labelledby="basic-tab">
                        <div class="card-user-info card  shadow mt-5 rounded-0 " >
                            <div class="card-body px-2">
                                <div class="d-flex justify-content-center">
                                    <h4 class=" text-center my-0">Professional Settings</h4>
                                </div>
                                <form action="">
                                    <div class="form-group mb-3 mt-3">
                                        <label for="">Employer</label>
                                        <input type="text" class="form-control rounded-0 shadow-none">
                                    </div>
                                    <div class="form-group mb-3 ">
                                        <label for="">Position</label>
                                        <input type="text" class="form-control rounded-0 shadow-none">
                                    </div>
                                    <div class="form-group mb-3 ">
                                        <label for="">Office Email</label>
                                        <input type="text" class="form-control rounded-0 shadow-none">
                                    </div>
                                    <div class="form-group mb-3 ">
                                        <label for="">Phone Number</label>
                                        <input type="text" class="form-control rounded-0 shadow-none">
                                    </div>
                                    <div class="form-group mb-3">
                                        <button class="btn bg-warning-light rounded-0">Save</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">...</div>
                    <div class="tab-pane fade" id="contact" role="tabpanel" aria-labelledby="contact-tab">...</div>
                  </div>
               
    
            </div>
        </div>
    </div>
</template>
<script>
import topNavBar from '../../components/TopNavBar/topNavBar.vue';
import sidebar from '../../components/SideBar/sidebar.vue'


export default {
    name:'settings',
    components:{
        topNavBar,
        sidebar
    },
    mounted(){
        this.$root.title = "Settings"
        document.title = "NovaGenesis | Settings"
    }
}
</script>