import { createApp } from 'vue'
import App from './App.vue'
import './assets/main.css'
import axios from 'axios'
import VueAxios from 'vue-axios'
import { createStore } from 'vuex'
createApp(App) 
    .use(VueAxios, axios)
    .mount('#app')
document.title = "VUE学习测试"