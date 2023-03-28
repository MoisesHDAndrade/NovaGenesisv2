<template>
    <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasSideBar" aria-labelledby="offcanvasSideBarLabel" style="z-index:9999">
        <div class="offcanvas-header">
            <h5 class="offcanvas-title fw-bold text-warning" id="offcanvasSideBarLabel">
                <span class="fw-bold">NovaGenesis</span>
            </h5>
            <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
            <div class="flex-shrink-0 p-3 bg-white" style="width: 280px;">
                <ul class="list-unstyled ps-0">
                  
                  <li class="mb-1">
                    <button class="btn btn-toggle align-items-center rounded " @click.prevent="goToDashboard">
                      Dashboard
                    </button>
                    <!-- <div class="collapse" id="dashboard-collapse" style="">
                      <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                        <li><a href="#" class="link-dark rounded">Overview</a></li>
                        <li><a href="#" class="link-dark rounded">Weekly</a></li>
                        <li><a href="#" class="link-dark rounded">Monthly</a></li>
                        <li><a href="#" class="link-dark rounded">Annually</a></li>
                      </ul>
                    </div> -->
                  </li>
                  <li class="mb-1">
                    <button class="btn btn-toggle align-items-center rounded" data-bs-dismiss="offcanvas"  @click.prevent="goToJobList">Job List</button>
                    
                    <!-- <div class="collapse" id="dashboard-collapse" style="">
                      <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                        <li><a href="#" class="link-dark rounded">Overview</a></li>
                        <li><a href="#" class="link-dark rounded">Weekly</a></li>
                        <li><a href="#" class="link-dark rounded">Monthly</a></li>
                        <li><a href="#" class="link-dark rounded">Annually</a></li>
                      </ul>
                    </div> -->
                  </li>
                  <li class="mb-1">
                    <button class="btn btn-toggle align-items-center rounded " data-bs-dismiss="offcanvas"  @click.prevent="goToTimesheetView">
                      Timesheet View
                    </button>
                    <!-- <div class="collapse" id="dashboard-collapse" style="">
                      <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                        <li><a href="#" class="link-dark rounded">Overview</a></li>
                        <li><a href="#" class="link-dark rounded">Weekly</a></li>
                        <li><a href="#" class="link-dark rounded">Monthly</a></li>
                        <li><a href="#" class="link-dark rounded">Annually</a></li>
                      </ul>
                    </div> -->
                  </li>
                  <li class="mb-1">
                    <button class="btn btn-toggle align-items-center rounded collapsed" data-bs-toggle="collapse" data-bs-target="#home-collapse" aria-expanded="false">
                      Employees
                    </button>
                    <div class="collapse" id="home-collapse" style="">
                      <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                        <li><a href="#" class="link-dark rounded">Overview</a></li>
                        <li><a href="#" class="link-dark rounded">Updates</a></li>
                        <li><a href="#" class="link-dark rounded">Reports</a></li>
                      </ul>
                    </div>
                  </li>
                  <li class="border-top my-3"></li>
                  <li class="mb-1">
                    <button class="btn btn-toggle align-items-center rounded collapsed" data-bs-toggle="collapse" data-bs-target="#account-collapse" aria-expanded="false">
                      Account
                    </button>
                    <div class="collapse" id="account-collapse">
                      <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                        <li><a href="#" class="link-dark rounded">New...</a></li>
                        <li><a href="#" class="link-dark rounded">Profile</a></li>
                        <li @click.prevent="goToSettings"><a @click.prevent="goToSettings" href="#" class="link-dark rounded">Settings</a></li>
                        <li><a href="#" class="link-dark rounded" @click.prevent="logout" data-bs-dismiss="offcanvas" >Sign out</a></li>
                      </ul>
                    </div>
                  </li>
                </ul>
              </div>
        </div>
    </div>
</template>
<script>
import store from '../../state/index'
export default {
    name:'sidebar',
    data(){
        return{

        }
    },
    methods:{
      logout(){
        store.dispatch('logoutUser');
        if(!store.getters.loggedIn){
          this.$router.push({ name: 'login' })
        }
      },
      goToJobList(){
        this.$router.push({ name: 'joblist' })
      },
      goToTimesheetView(){
        this.$router.push({ name: 'timesheet' })
      },
      goToDashboard(){
        this.$router.push({ name: 'dashboard' })
      },
      goToSettings(){
        this.$router.push({ name: 'settings' })
      },
    }
}
</script>