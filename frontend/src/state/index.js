import { createStore } from 'vuex';
import axios from 'axios';
import router from '../router/index';
// import jwt_decode from 'jwt-decode';
const BASE_URL = "//localhost:8000";
// const BASE_URL = "https://e9cd-101-98-135-159.au.ngrok.io/";

const axiosBase = axios.create({
  baseURL: BASE_URL,
  headers: { contentType: 'application/json' }
});


axiosBase.interceptors.response.use(undefined, function (err) {
  // if error response status is 401, it means the request was invalid due to expired access token
  console.log(err.response.status);
  if (err.config && err.response && err.response.status === 401) {
  // if (err.config && err.response && err.response.status === 404) {
    store.dispatch('refreshToken') // attempt to obtain new access token by running 'refreshToken' action
      .then(access => {
        // if successful re-send the request to get the data from server
        axiosBase.request({
          baseURL: BASE_URL,
          method: 'get',
          headers: { Authorization: `Bearer ${access}` }, // the new access token is attached to the authorization header
          url: '/#/login'
        }).then(response => {
          console.log('promise check');
          // if successfully received the data store it in store.state.APIData so that 'Downloads' component can grab the
          // data from it and display to the client.
          store.state.APIData = response.data;
        }).catch(err => {
          console.log('Got the new access token but error while trying to fetch data from the API using it');
          
          return Promise.reject(err);
        });
      })
      .catch(err => {
        return Promise.reject(err);
      });
  }
});

const store = createStore({
    state() {
        return{
            accessToken: localStorage.getItem('access_token') || null, // makes sure the user is logged in even after
            // refreshing the page
            refreshToken: localStorage.getItem('refresh_token') || null,
            APIData: '' // received data from the backend API is stored here.
        
     
        };
    },
    getters: {
            loggedIn (state) {
              return state.accessToken !== null;
            }
          },
    mutations: {
     
		updateLocalStorage (state, { access, refresh }) {
			localStorage.setItem('access_token', access);
			localStorage.setItem('refresh_token', refresh);
			state.accessToken = access;
			state.refreshToken = refresh;
		},
		updateAccess (state, access) {
			state.accessToken = access;
		},
		destroyToken (state) {
			state.accessToken = null;
			state.refreshToken = null;
		}
    },
    actions:{
       
        refreshToken (context) {
			return new Promise((resolve, reject) => {
				axiosBase.post('/api/token/refresh/', {
					refresh: context.state.refreshToken
				}) // send the stored refresh token to the backend API
					.then(response => { // if API sends back new access and refresh token update the store
					// console.log('New access successfully generated');
					context.commit('updateAccess', response.data.access);
					Promise.resolve(response.data.access);
					// console.log(response.data.access);
					})
					.catch(err => {
					// console.log('error in refreshToken Task');
					router.replace({ name: 'login' });
					context.commit('destroyToken');
					// error generating new access and refresh token because refresh token has expired
					reject(err);
				});
			});
			},
		registerUser (context, data) {
			return new Promise((resolve, reject) => {
				axiosBase.post('/register/', {
					name: data.name,
					email: data.email,
					username: data.username,
					password: data.password,
					confirm: data.confirm
				})
					.then(response => {
						resolve(response);
					})
					.catch(error => {
						reject(error);
				});
			});
		},
		logoutUser (context) {
			if (context.getters.loggedIn) {
				axiosBase.get('/api/token/logout/')
				.then(() => {
					localStorage.removeItem('access_token');
					localStorage.removeItem('refresh_token');
					context.commit('destroyToken');
					router.push({ name: 'login' });
				})
				.catch(err => {
					localStorage.removeItem('access_token');
					localStorage.removeItem('refresh_token');
					context.commit('destroyToken');
					console.log(err);
				});
			}
		},
       
        loginUser (context, credentials) {
			return new Promise((resolve, reject) => {
				axiosBase.post('/api/token/', {
				username: credentials.username,
				password: credentials.password
				})
				// if successful update local storage:
				.then(response => {
					context.commit('updateLocalStorage', { access: response.data.access, refresh: response.data.refresh }) ;// store the access and refresh token in localstorage
					resolve();
					router.push({ name: 'dashboard' });
				})
				.catch(err => {
					reject(err);
				});
			});
    }
      }
    });

export default store;