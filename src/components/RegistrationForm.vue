<template>
  <div class="form-body">
    <h1 class="auth-form-title form-body__title">Регистрация</h1>
    <el-form ref="formInstance" :model="formModel" :rules="formRules" class="">
      <el-form-item label="Почта" prop="email">
        <el-input v-model="formModel.email"></el-input>
      </el-form-item>
      <el-form-item label="Имя" prop="first_name">
        <el-input v-model="formModel.first_name"></el-input>
      </el-form-item>
      <el-form-item label="Фамилия" prop="last_name">
        <el-input v-model="formModel.last_name"></el-input>
      </el-form-item>
      <el-form-item label="Номер комнаты" prop="room_number">
        <el-input v-model.number="formModel.room_number"></el-input>
      </el-form-item>
      <el-form-item label="Пароль" prop="password">
        <el-input v-model="formModel.password" type="password" />
      </el-form-item>
      <div class="flex space-between">
        <router-link :to="{ name: 'login' }">Вход</router-link>
        <el-form-item class="flex space-between">
          <el-button type="primary" @click="submitForm(formInstance)">Зарегистрироваться</el-button>
        </el-form-item>
      </div>
    </el-form>
  </div>
</template>

<script lang="ts" setup>
import type { RegisterForm } from '@/types/auth';
import type { FormInstance, FormRules } from 'element-plus';
import { reactive, ref } from 'vue';
import {
  email_validate_rules,
  fisrt_name_validate_rules,
  last_name_validate_rules,
  password_validate_rules,
  room_number_validate_rules
} from '@/validators/auth';
import { errorMessage, successMessage } from '@/presets/messages';

const formInstance = ref<FormInstance>();
const formModel = reactive<RegisterForm>({
  email: '',
  first_name: '',
  last_name: '',
  password: '',
  room_number: null
});
const formRules = reactive<FormRules>({
  first_name: fisrt_name_validate_rules,
  last_name: last_name_validate_rules,
  email: email_validate_rules,
  password: password_validate_rules,
  room_number: room_number_validate_rules
});

const submitForm = (form: FormInstance) => {
  if (!form) return;
  form.validate((valid) => {
    if (valid) {
      successMessage();
    } else {
      errorMessage();
    }
  });
};
</script>
