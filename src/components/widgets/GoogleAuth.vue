<template>
  <button @click="handleUserGoogleAuthorization">Login Using Google</button>
  <el-dialog v-model="dialogVisible" title="Завершите регистрацию">
    <google-registration-form />
  </el-dialog>
</template>

<script lang="ts" setup>
import { googleAuthCodeLogin } from 'vue3-google-login';
import { GoogleRegistrationFormType } from '@/types/authFormTypes';
import { provide, ref } from 'vue';
import GoogleRegistrationForm from '@/components/Forms/GoogleRegistrationForm.vue';
import { authApi } from '@/api/KY/AuthService/auth.api';

const dialogVisible = ref(false);

const handleUserGoogleAuthorization = async () => {
  const googleData = await googleAuthCodeLogin();
  const [error, data] = await authApi.loginGoogleUser(googleData.code);

  if (!error && data) {
    const { is_register, access, refresh } = data;

    localStorage.setItem('refreshToken', refresh);

    localStorage.setItem('accessToken', access);

    if (!is_register) {
      dialogVisible.value = true;
    }
  }
};

const handleUserGoogleRegister = async (form: GoogleRegistrationFormType) => {
  const [error, data] = await authApi.registerGoogleUser(form);

  if (!error) {
    const { is_register, refresh, access } = data;

    if (is_register) {
      localStorage.setItem('refreshToken', refresh);

      localStorage.setItem('accessToken', access);
    }

    dialogVisible.value = false;
  }
};

provide('handleUserGoogleRegister', handleUserGoogleRegister);
</script>
