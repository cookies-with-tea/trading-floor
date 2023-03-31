<template>
  <div class="form">
    <h1 class="ta-c form-body__title">Вход</h1>
    <el-form ref="loginFormInstance" :model="loginFormModel" :rules="loginFormRules" class="">
      <el-form-item label="Почта" prop="email">
        <el-input v-model="loginFormModel.email" />
      </el-form-item>
      <el-form-item label="Пароль" prop="password">
        <el-input v-model="loginFormModel.password" type="password" />
      </el-form-item>
      <div class="d-f jc-sb ai-c">
        <router-link :to="{ name: routeNames.RegistrationPage }">Регистрация</router-link>
        <el-form-item class="mb-0">
          <el-button type="primary" @click="handleUserSignIn">Войти</el-button>
        </el-form-item>
      </div>
    </el-form>
  </div>
</template>

<script lang="ts" setup>
import type { LoginFormType } from '@/types/authFormTypes';
import { FormInstance, FormRules } from 'element-plus';
import { reactive, ref } from 'vue';
import { requiredRule } from '@/constants/formRules';
import { ROUTE_NAMES } from '@/constants/routeNames';
import { authApi } from '@/api/auth/auth.api';
import { useAuthStore } from '@/stores/authStore';

const authStore = useAuthStore();
const loginFormInstance = ref<FormInstance>();
const routeNames = ROUTE_NAMES;

const loginFormModel = reactive<LoginFormType>({
  email: '',
  password: '',
});

const loginFormRules = reactive<FormRules>({
  email: [requiredRule],
  password: [requiredRule],
});

async function handleUserSignIn() {
  const [error, data] = await authApi.authUser(loginFormModel);

  if (!error) {
    const { access, refresh } = data;

    authStore.refreshToken = refresh;

    localStorage.setItem('accessToken', access);
  }
}
</script>
