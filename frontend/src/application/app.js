// // This is the scss entry file
import "../styles/index.scss";
import "../styles/index.css";

// // We can import Bootstrap JS instead of the CDN link, if you do not use
// // Bootstrap, please feel free to remove it.
import "bootstrap/dist/js/bootstrap.bundle";
import vSelect from 'vue-select';


import { createApp } from 'vue';



import App from '../components/App.vue';
import router from '../router';
import store from '../state/index';
// import './assets/main.css';
const app = createApp(App);
app.component( 'v-select', vSelect );
app.use(store);
app.use(router);


app.mount('#app');


