import { createRouter, createWebHistory } from 'vue-router';
import AuthorizationLayout from '@/layouts/AuthorizationLayout.vue';
import DefaultLayout from '@/layouts/DefaultLayout.vue';
import { ROUTE_NAMES } from '@/constants/routeNames';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: AuthorizationLayout,
      redirect: { name: ROUTE_NAMES.LoginPage },
      children: [
        {
          path: 'registration',
          name: ROUTE_NAMES.RegistrationPage,
          component: () => import('@/pages/RegistrationPage.vue'),
        },
        {
          path: 'login',
          name: ROUTE_NAMES.LoginPage,
          component: () => import('@/pages/LoginPage.vue'),
        },
      ],
    },
    {
      path: '/',
      component: DefaultLayout,
      children: [
        {
          path: '/',
          name: ROUTE_NAMES.HomePage,
          component: () => import('@/pages/HomePage.vue'),
        },
      ],
    },
  ],
});

export default router;
