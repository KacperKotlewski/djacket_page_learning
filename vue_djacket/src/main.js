import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios";

const API_URL = "http://192.168.1.11:8000"
axios.defaults.baseURL = API_URL

const app = createApp(App);

app.config.globalProperties.API_URL = API_URL

app.use(store).use(router, axios).mount('#app')
