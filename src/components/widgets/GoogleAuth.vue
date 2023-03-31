<template>
  <button @click="handleUserGoogleAuthorization">Login Using Google</button>
</template>

<script lang="ts" setup>
import { googleAuthCodeLogin } from 'vue3-google-login';
import { authApi } from '@/api/auth/auth.api';
import { useAuthStore } from '@/stores/authStore';

const authStore = useAuthStore();

const handleUserGoogleAuthorization = async () => {
  const googleData = await googleAuthCodeLogin();
  const [error, data] = await authApi.authGoogleUser(googleData.code);

  if (!error && data) {
    const { access, refresh } = data;

    authStore.refreshToken = refresh;

    localStorage.setItem('accessToken', access);
  }
};
</script>

<style lang="scss" scoped></style>
