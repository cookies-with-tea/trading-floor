import { createRouter, createWebHistory } from 'vue-router';
import DefaultLayout from '@/layouts/DefaultLayout.vue';
import { ROUTE_NAMES } from '@/constants/routeNames';

const router = createRouter({
  history: createWebHistory(),
  routes: [
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
