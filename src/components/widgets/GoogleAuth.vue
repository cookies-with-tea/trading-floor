<template>
  <button @click="handleUserGoogleAuthorization">Login Using Google</button>
  <el-dialog v-model="dialogVisible" title="Завершите регистрацию">
    <google-registration-form />
  </el-dialog>
</template>

<script lang="ts" setup>
import { googleAuthCodeLogin } from 'vue3-google-login';
import { authApi } from '@/api/auth/auth.api';
import { useAuthStore } from '@/stores/authStore';
import { GoogleRegistrationFormType } from '@/types/authFormTypes';
import { provide, ref } from 'vue';
import GoogleRegistrationForm from '@/components/Forms/GoogleRegistrationForm.vue';

const authStore = useAuthStore();
const dialogVisible = ref(false);

const handleUserGoogleAuthorization = async () => {
  const googleData = await googleAuthCodeLogin();
  const [error, data] = await authApi.authGoogleUser(googleData.code);

  if (!error && data) {
    const { isActive, access, refresh } = data;

    authStore.refreshToken = refresh;

    localStorage.setItem('accessToken', access);

    if (!isActive) {
      dialogVisible.value = true;
    }
  }
};

const handleUserGoogleRegister = async (form: GoogleRegistrationFormType) => {
  const [error, data] = await authApi.confirmGoogleUser(form);

  if (!error) {
    const { isActive, refresh, access } = data;

    if (isActive) {
      authStore.refreshToken = refresh;

      localStorage.setItem('accessToken', access);
    }
  }
};

provide('handleUserGoogleRegister', handleUserGoogleRegister);
</script>

<style lang="scss" scoped></style>
