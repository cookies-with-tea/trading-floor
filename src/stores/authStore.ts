import { defineStore } from 'pinia';
import { ref } from 'vue';
import { UserType } from '@/types/userTypes';

export const useAuthStore = defineStore('auth', () => {
  const refreshToken = ref('');
  const user = ref<UserType>();

  return { refreshToken, user };
});
