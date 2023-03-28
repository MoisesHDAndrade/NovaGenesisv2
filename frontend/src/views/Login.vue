<template>
<div>
	<div class="container-fluid">
		<div class="d-flex justify-content-center align-items-center my-5 main-container-hide">
			<div class="col-lg-8 col-xl-8 col-md-12 col-xs-12 col-sm-12 col-12">
				<div class="row justify-content-center">
					<h1 class="display-5 text-center text-dark"><span class="fw-bold p-2">NovaGenesis</span> </h1>
					<div class="col-12 text-center py-3">
						<h5 class="card-title text-center mb-0">Welcome back</h5>
						<p class="text-muted m-0">Enter your details to log in</p>
					</div>
				</div>
				<!-- <div class="card shadow bg-light rounded-3 p-0">
					<div class="card-body  px-2"> -->
						<div class="row">
							<div class="col-12 my-2">
								<label for="">Username</label>
								<input type="text" class="form-control rounded-3" v-model="username">
							</div>
						</div>
						<div class="row">
							<div class="col-12 my-2">
								<label for="">Password</label>
								<input type="password" class="form-control rounded-3"  v-model="password">
							</div>
						</div>
						<div class="row">
							<div class="col-12 my-2 text-end">
								<a href="" class=" fw-bold text-dark" >Forgot Password?</a>
							</div>
						</div>
						<div class="row">
							<div class="col-12 my-2 ">
								<button class="btn  text-dark w-100 rounded-3 shadow" @click="loginUser" type="button" style="background-color: rgba(255, 193, 7,0.4)">
									<div class="d-flex justify-content-center align-items-center">
										<span class="mx-2" v-if="!loading">Log in</span>
										<span class="spinner-border fw-light" style="width:1.5em;height:1.5em"  role="status" aria-hidden="true" v-else></span>
  										<span class="visually-hidden">Loading...</span>
									</div>
								</button>
							</div>
						</div>
						<div class="row">
							<div class="col-12 my-2 text-center">
								<div class="d-flex justify-content-center align-items-center">
									<div class="border-top w-100"></div>
									<div class="mx-3">or</div>
									<div class="border-top w-100"></div>
								</div>
							</div>
						</div>
						<div class="row">
							<div class="col-12 my-2 ">
								<RouterLink class="btn btn-outline-dark rounded-3 w-100 shadow" to="signup">Sign up</RouterLink>
							</div>
						</div>
					</div>
				<!-- </div>
			</div> -->
		</div>
	</div>
</div>
</template>
<script>
import store from '../state/index'
export default {
  name:'login',
  data(){
	return{
		username:"",
		password:"", 
		loading: false
	}
  },
  methods:{
	loadAnimation(){
		let mainContainer = document.getElementsByClassName("main-container-hide")[0]
		setTimeout(()=>{
			mainContainer.classList.add("main-container-show")
		},300)
	},

	loginUser(){
		if(!this.username || !this.password) return
		this.loading = true
		store.dispatch('loginUser', {
              username: this.username,
              password: this.password
            }).then(response => {
                  setTimeout(()=>{
                    this.$router.push({ name: 'dashboard' })
                  },1000)
                })
              .catch(err => {
                    if(err.response.status == 401){
                        this.loading = false
                       
                    }
              })
	}
  },
  mounted(){
	this.loadAnimation()
	
  }
}

</script>
<style scoped>
body{
	/*background-color: #222f3e;*/

}
.btn-purple{
	background-color: #6f42c1;
}
.main-container-hide{
	right:50em;
	position: relative;
	transition: .5s ease-in-out;
	opacity: 0.1;
}
.main-container-show{
	right:0em;
	position: relative;
	transition: .5s ease-in-out;
	opacity: 1;
}
</style>