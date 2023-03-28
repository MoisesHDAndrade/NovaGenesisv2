import { createRouter, createWebHistory } from 'vue-router';
import store from "../state/index";
// import { createRouter,  } from 'vue-router';

const router = createRouter({
  history: createWebHistory('#'),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/Login.vue')
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('../views/SignUp.vue')
    },
    {
      path: '/joblist',
      name: 'joblist',
      component: () => import('../views/Job/index.vue'),
      meta: {
        requiresAuth: true
      },
    },
    {
      path: '/jobdetail/:id',
      name: 'jobdetail',
      component: () => import('../views/JobDetail/index.vue'),
      meta: {
        requiresAuth: true
      },
    },
    {
      path: '/message',
      name: 'message',
      component: () => import('../components/messageContainer.vue'),
      meta: {
        requiresAuth: true
      },
    },
    {
      path: '/settings',
      name: 'settings',
      component: () => import('../views/Settings/index.vue'),
      meta: {
        requiresAuth: true
      },
    },
    {
      path: '/timesheet',
      name: 'timesheet',
      component: () => import('../views/Timesheet/index.vue'),
      meta: {
        requiresAuth: true
      },
    },
    {
      path: '/',
      name: 'dashboard',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded w../views/Dashboard.vueed.
      component: () => import('../views/Dashboard/index.vue'),
      meta: {
        requiresAuth: true
      },
    },
  ]
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    
    if (!store.getters.loggedIn) {
     
      next({ name: 'login' });

    } 
    else {
      store.dispatch('refreshToken');
     
      next();
    }
  } else if (to.matched.some(record => record.meta.requiresLogged)) {
    // else if any of the routes in ./router.js has a meta named 'requiresLogged: true'
    // then check if the user is logged in; if true continue to home page else continue routing to the destination path
    // this comes to play if the user is logged in and tries to access the login/register page
    if (store.getters.loggedIn) {
      next({ name: 'dashboard' });

    } else {
      
      next();
    }
  } else {
    next();
  }
  // var modals = document.getElementsByClassName("modal");
  // for(var item of modals){
  //     item.dismiss();
  // }
});
export default router;