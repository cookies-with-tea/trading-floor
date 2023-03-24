<template>
  <div class="form-body">
    <h1 class="auth-form-title form-body__title">Регистрация</h1>
    <el-form ref="formInstance" :model="formModel" :rules="formRules" class="">
      <el-form-item label="Почта" prop="email">
        <el-input v-model="formModel.email" />
      </el-form-item>
      <el-form-item label="Имя" prop="first_name">
        <el-input v-model="formModel.first_name" />
      </el-form-item>
      <el-form-item label="Фамилия" prop="last_name">
        <el-input v-model="formModel.last_name" />
      </el-form-item>
      <el-form-item label="Номер комнаты" prop="room_number">
        <el-input v-model.number="formModel.room_number" />
      </el-form-item>
      <el-form-item label="Пароль" prop="password">
        <el-input v-model="formModel.password" type="password" />
      </el-form-item>
      <div class="d-f jc-sb ai-c">
        <router-link :to="{ name: ROUTE_NAMES.LoginPage }">Вход</router-link>
        <el-form-item class="mb-0">
          <el-button type="primary" @click="submitForm(formInstance)">Зарегистрироваться</el-button>
        </el-form-item>
      </div>
    </el-form>
  </div>
</template>

<script lang="ts" setup>
import type { RegisterFormType } from '@/types/authFormTypes';
import { ElMessage, FormInstance, FormRules } from 'element-plus';
import { reactive, ref } from 'vue';
import { userApi } from '@/api/user/user.api';
import { ROUTE_NAMES } from '@/constants/routeNames';
import {
  emailRules,
  firstNameRules,
  lastNameRules,
  passwordRules,
  requiredRule,
  roomNumberRules,
} from '@/constants/formRules';

const formInstance = ref<FormInstance>();

const formModel = reactive<RegisterFormType>({
  email: '',
  first_name: '',
  last_name: '',
  password: '',
  room_number: null,
});

const formRules = reactive<FormRules>({
  first_name: [requiredRule, ...firstNameRules],
  last_name: [...lastNameRules],
  email: [requiredRule, ...emailRules],
  password: [requiredRule, ...passwordRules],
  room_number: [requiredRule, ...roomNumberRules],
});

async function submitForm(form: FormInstance | undefined) {
  if (!form) return;
  await form.validate(async (valid) => {
    if (valid) {
      const [error] = await userApi.registerUser(formModel);

      if (error !== null) {
        ElMessage({
          type: 'success',
          message: 'Данные отправлены',
        });
      } else {
        ElMessage({
          type: 'error',
          message: `${error}`,
        });
      }
    }
  });
}
</script>
