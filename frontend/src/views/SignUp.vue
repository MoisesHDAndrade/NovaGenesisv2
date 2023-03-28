<template>
<div>
	<div class="container-fluid">
		<div class="d-flex justify-content-center align-items-center my-5 main-container-hide">
			<div class="col-lg-8 col-xl-8 col-md-12 col-xs-12 col-sm-12 col-12">
				<div class="row justify-content-center">
					<h1 class="display-5 text-center text-warning fw-bold">NovaGenesis </h1>
				</div>
				<div class="card shadow bg-light ">
					<div class="card-body ">
						<div class="row">
							<div class="col-12">
								<h5 class="card-title te">Sign up</h5>
							</div>
						</div>
						<div class="row">
							<div class="col-12 my-2">
								<input type="text" class="form-control" placeholder="First Name" required>
							</div>
						</div>
						<div class="row">
							<div class="col-12 my-2">
								<input type="text" class="form-control" placeholder="Last Name" required>
							</div>
						</div>
						<div class="row">
							<div class="col-12 my-2">
								<input type="email" class="form-control" placeholder="Email" required>
							</div>
						</div>
						<div class="row">
							<div class="col-12 my-2">
								<input type="text" class="form-control" placeholder="Username">
							</div>
						</div>
						<div class="row">
							<div class="col-12 my-2">
								<input type="password" class="form-control" placeholder="Password">
							</div>
						</div>
						<div class="row">
							<div class="col-12 my-2">
								<input type="password" class="form-control" placeholder="Confirm Password">
							</div>
						</div>
						
						<div class="row">
							<div class="col-12 my-2 ">
								<button class="btn btn-dark  w-100">Sign up</button>
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
								<RouterLink class="btn btn-outline-dark  w-100" to="login">Log in</RouterLink>
							</div>
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
  name:'signup',
  data(){
	return{

	}
  },
  methods:{
	loadAnimation(){
		let mainContainer = document.getElementsByClassName("main-container-hide")[0]
		setTimeout(()=>{
			mainContainer.classList.add("main-container-show")
		},300)
	}
  },
  mounted(){
	this.loadAnimation()
  }
}

</script>
<style scoped>
body{
	/*background-color: #6f42c1;*/
	background-color: #222f3e;

}
.btn-purple{
	background-color: #6f42c1;
}
.main-container-hide{
	left:50em;
	position: relative;
	transition: .5s ease-in-out;
	opacity: 0.1;
}
.main-container-show{
	left:0em;
	position: relative;
	transition: .5s ease-in-out;
	opacity: 1;
}
</style>