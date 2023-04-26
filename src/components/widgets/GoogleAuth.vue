<template>
  <div class="google-auth">
    <div class="google-auth__body">
      <el-button class="background w-100" type="primary" @click="handleUserGoogleAuthorize">
        Войти с помощью Google
        <icon-template class="icon-20 ml-10" name="google" />
      </el-button>
    </div>

    <base-dialog v-model="isRegistrationDialogVisible">
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

const isRegistrationDialogVisible = ref(true);

const handleUserGoogleAuthorize = async () => {
  const googleData = await googleAuthCodeLogin();
  const [error, data] = await authApi.loginGoogleUser(googleData.code);

  if (!error && data) {
    const { is_register, access, refresh } = data;

    const { setAccess, setRefresh } = useTokens(localStorage);

    setRefresh(refresh);

    setAccess(access);

    if (!is_register) {
      isRegistrationDialogVisible.value = true;
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

    isRegistrationDialogVisible.value = false;
  }
};

provide('handleUserGoogleRegister', handleUserGoogleRegister);
</script>

<style lang="scss" scoped>
.google-auth {
  display: flex;
  justify-content: center;

  :deep(.el-dialog) {
    width: 100% !important;
    max-width: 500px !important;
  }

  &__body {
    width: 100%;
    max-width: 400px;
  }
}
</style>
