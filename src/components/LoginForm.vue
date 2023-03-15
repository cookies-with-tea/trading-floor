<template>
  <div class="form-body">
    <h1 class="auth-form-title form-body__title">Вход</h1>
    <el-form ref="formInstance" :model="formModel" :rules="formRules" class="">
      <el-form-item label="Почта" prop="email">
        <el-input v-model="formModel.email" />
      </el-form-item>
      <el-form-item label="Пароль" prop="password">
        <el-input v-model="formModel.password" type="password" />
      </el-form-item>
      <div class="d-f jc-sb ai-c">
        <router-link :to="{ name: ROUTE_NAMES.RegistrationPage }">Регистрация</router-link>
        <el-form-item class="mb-0">
          <el-button type="primary">Войти</el-button>
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

const formInstance = ref<FormInstance>();

const formModel = reactive<LoginFormType>({
  email: '',
  password: '',
});

const formRules = reactive<FormRules>({
  email: [requiredRule],
  password: [requiredRule],
});
</script>
