import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useAuthStore = defineStore('auth', () => {
  const refreshToken = ref('');

  return { refreshToken };
});
