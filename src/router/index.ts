import { createRouter, createWebHistory } from 'vue-router';
import AuthLayout from '@/layouts/AuthLayout.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: AuthLayout,
      children: [
        {
          path: 'registration',
          name: 'registration',
          component: () => import('@/components/RegistrationForm.vue')
        },
        {
          path: 'login',
          name: 'login',
          component: () => import('@/components/LoginForm.vue')
        }
      ]
    }
  ]
});

export default router;
