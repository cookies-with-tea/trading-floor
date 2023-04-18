<template>
  <div class="google-auth">
    <el-button type="primary" @click="handleUserGoogleAuthorization">Login Using Google</el-button>
    <base-dialog v-model="dialogVisible" class="google-auth__dialog">
      <h2 class="ta-c">Введите свои данные</h2>
      <google-registration-form class="mt-30" />
    </base-dialog>
  </div>
</template>

<script lang="ts" setup>
import { googleAuthCodeLogin } from 'vue3-google-login';
import { GoogleRegistrationFormType } from '@/types/authFormTypes';
import { provide, ref } from 'vue';
import GoogleRegistrationForm from '@/components/Forms/GoogleRegistrationForm.vue';
import { authApi } from '@/api/KY/AuthService/auth.api';
import { useTokens } from '@/composables/useTokens';

const dialogVisible = ref(false);

const handleUserGoogleAuthorization = async () => {
  const googleData = await googleAuthCodeLogin();
  const [error, data] = await authApi.loginGoogleUser(googleData.code);

  if (!error && data) {
    const { is_register, access, refresh } = data;

    const { setAccess, setRefresh } = useTokens(localStorage);

    setRefresh(refresh);

    setAccess(access);

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
      const { setAccess, setRefresh } = useTokens(localStorage);

      setRefresh(refresh);

      setAccess(access);
    }

    dialogVisible.value = false;
  }
};

provide('handleUserGoogleRegister', handleUserGoogleRegister);
</script>

<style lang="scss" scoped>
.google-auth {
  &__dialog {
    width: 100% !important;
    max-width: 500px !important;
  }

  :deep(.el-dialog) {
    width: 100% !important;
    max-width: 500px !important;
  }
}
</style>
