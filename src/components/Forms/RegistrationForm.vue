<template>
  <div class="form">
    <h1 class="ta-c form-body__title">Регистрация</h1>
    <el-form ref="registrationFormInstance" :model="registrationFormModel" :rules="registrationFormRules" class="">
      <el-form-item label="Почта" prop="email">
        <el-input v-model="registrationFormModel.email" />
      </el-form-item>
      <el-form-item label="Имя" prop="firstName">
        <el-input v-model="registrationFormModel.firstName" />
      </el-form-item>
      <el-form-item label="Фамилия" prop="lastName">
        <el-input v-model="registrationFormModel.lastName" />
      </el-form-item>
      <el-form-item label="Номер комнаты" prop="roomNumber">
        <el-input v-model.number="registrationFormModel.roomNumber" />
      </el-form-item>
      <el-form-item label="Пароль" prop="password">
        <el-input v-model="registrationFormModel.password" type="password" />
      </el-form-item>
      <div class="d-f jc-sb ai-c">
        <router-link :to="{ name: routeNames.LoginPage }">Вход</router-link>
        <el-form-item class="mb-0">
          <el-button type="primary" @click="handleUserSignUp">Зарегистрироваться</el-button>
        </el-form-item>
      </div>
    </el-form>
  </div>
</template>

<script lang="ts" setup>
import type { RegisterFormType } from '@/types/authFormTypes';
import { FormInstance, FormRules } from 'element-plus';
import { reactive, ref } from 'vue';
import { userApi } from '@/api/user/user.api';
import {
  emailRules,
  firstNameRules,
  lastNameRules,
  passwordRules,
  requiredRule,
  roomNumberRules,
} from '@/constants/formRules';
import { ROUTE_NAMES } from '@/constants/routeNames';

const registrationFormInstance = ref<FormInstance>();
const routeNames = ref(ROUTE_NAMES);

const registrationFormModel = reactive<RegisterFormType>({
  email: '',
  firstName: '',
  lastName: '',
  password: '',
  roomNumber: null,
});

const registrationFormRules = reactive<FormRules>({
  firstName: [requiredRule, ...firstNameRules],
  lastName: [...lastNameRules],
  email: [requiredRule, ...emailRules],
  password: [requiredRule, ...passwordRules],
  roomNumber: [requiredRule, ...roomNumberRules],
});

async function handleUserSignUp() {
  if (!registrationFormInstance.value) return;
  await registrationFormInstance.value.validate(async (valid) => {
    if (valid) {
      await userApi.registerUser(registrationFormModel);
    }
  });
}
</script>
