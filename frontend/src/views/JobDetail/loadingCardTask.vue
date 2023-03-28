<template>
	<div class="col-md-12 col-xs-12 col-sm-12 col-xl-12 col-lg-12  " style="padding-bottom:4rem">
        <div class="row w-100 mx-auto">
          <div class="col-md-12 col-xs-12 col-sm-12 col-xl-4 col-lg-4 my-1 " v-for="item in 6" :key="item">
              <div class="card shadow bg-light  rounded-3 overflow-hidden"  >
                  <div class="card-body p-0 " >
                      <div class="position-relative placeholder-glow">
                          <div class="bg-light border-bottom " style="position: relative; display: block;width: 100%; height: 100%;z-index: 2;">
                              <div style="" class="p-3 d-flex justify-content-between placeholder-glow">
                                  <span class="display-6 placeholder col-4 "></span>
                              </div>
                          </div>
                      </div>
                      <div class="d-flex justify-content-between align-items-center px-3 py-0 mt-2">
                          <div class="col-12 me-1">
                              <div class="row w-100 justify-content-between align-items-center position-relative">
									<div class="row placeholder-glow w-100 px-4">
										<span class=" placeholder col-12 w-100"></span>
									</div>
									<div class="row w-100 placeholder-glow w-100 px-4 mt-3">
										<span class=" placeholder col-12 w-25"></span>
									</div>
                              </div>
                          </div>
                      </div>
                      <div class="px-1 mb-2">
                          <button  class="btn btn-sm placeholder-glow shadow rounded-3 w-100 mt-3" style="background-color: rgba(255, 193, 7,0.4)" >
                              <div class=" d-flex align-items-center justify-content-center ">
                                   ........
                              </div> 
                          </button>
                      </div>
                  </div>
              </div>
          </div>
		</div>
   </div>
</template>