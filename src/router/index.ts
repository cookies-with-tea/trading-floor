import { createRouter, createWebHistory } from 'vue-router';
import AuthorizationLayout from '@/layouts/AuthorizationLayout.vue';
import DefaultLayout from '@/layouts/DefaultLayout.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/authorization',
      component: AuthorizationLayout,
      redirect: { name: 'TheLogin' },
      children: [
        {
          path: 'registration',
          name: 'TheRegistration',
          component: () => import('@/components/Forms/RegistrationForm.vue'),
        },
        {
          path: 'login',
          name: 'TheLogin',
          component: () => import('@/components/Forms/LoginForm.vue'),
        },
      ],
    },
    {
      path: '/',
      component: DefaultLayout,
      children: [
        {
          path: '/',
          name: 'TheHome',
          component: () => import('@/pages/HomePage.vue'),
        },
      ],
    },
  ],
});

export default router;
