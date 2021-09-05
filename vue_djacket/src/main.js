import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios";
require("dotenv").config();

const AXIOS_ADDRESS_ENV = process.env.VUE_APP_AXIOS_ADDRESS

const API_URL = (AXIOS_ADDRESS_ENV) ? AXIOS_ADDRESS_ENV : "http://localhost:8000";
axios.defaults.baseURL = API_URL

const app = createApp(App);

app.config.globalProperties.API_URL = API_URL

app.use(store).use(router, axios).mount('#app')
