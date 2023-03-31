import { createRouter, createWebHistory } from 'vue-router';
import AuthorizationLayout from '@/layouts/AuthorizationLayout.vue';
import DefaultLayout from '@/layouts/DefaultLayout.vue';
import { ROUTE_NAMES } from '@/constants/routeNames';

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
          name: ROUTE_NAMES.RegistrationPage,
          component: () => import('@/components/Forms/RegistrationFormPage.vue'),
        },
        {
          path: 'login',
          name: ROUTE_NAMES.LoginPage,
          component: () => import('@/components/Forms/LoginFormPage.vue'),
        },
      ],
    },
    {
      path: '/',
      component: DefaultLayout,
      children: [
        {
          path: '/',
          name: ROUTE_NAMES.LoginPage,
          component: () => import('@/pages/HomePage.vue'),
        },
      ],
    },
  ],
});

export default router;
