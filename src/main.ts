import { createApp } from 'vue';
import { createPinia } from 'pinia';

import IconTemplate from '@/components/common/IconTemplate.vue';

import 'virtual:svg-icons-register';

// TODO: После подключения шрифтов убрать комментарий.
// import 'virtual:fonts.css'
import App from './App.vue';
import router from './router';
import ElementPlus from 'element-plus';
import vue3GoogleLogin from 'vue3-google-login';

import '@/styles/index.scss';

const app = createApp(App);

app.component('IconTemplate', IconTemplate);

app.use(createPinia());

app.use(router);

app.use(ElementPlus);

app.use(vue3GoogleLogin, {
  clientId: import.meta.env.VITE_GOOGLE_CLIENT_ID,
});

app.mount('#app');
