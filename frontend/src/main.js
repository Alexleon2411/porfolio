
import 'bootstrap/dist/css/bootstrap.css';
import { createApp } from "vue";
import { registerPlugins } from '@/plugins'
import axios from 'axios';

import App from './App.vue';
import router from './router';
import store from './store';

const app = createApp(App);

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:3050/';  // the FastAPI backend
registerPlugins(app)
app.use(router);
app.use(store);
app.mount("#app");
