<template>
  <div class="form">
    <h1 class="ta-c form-body__title">Регистрация</h1>
    <el-form
      ref="googleRegistrationFormInstance"
      :model="googleRegistrationFormModel"
      :rules="googleRegistrationFormRules"
      class=""
    >
      <el-form-item label="Имя" prop="firstName">
        <el-input v-model="googleRegistrationFormModel.firstName" />
      </el-form-item>
      <el-form-item label="Фамилия" prop="lastName">
        <el-input v-model="googleRegistrationFormModel.lastName" />
      </el-form-item>
      <el-form-item label="Номер комнаты" prop="roomNumber">
        <el-input v-model.number="googleRegistrationFormModel.roomNumber" />
      </el-form-item>
      <el-button type="primary" @click="handleGoogleRegistrationFormSubmit">Зарегистрироваться</el-button>
    </el-form>
  </div>
</template>

<script lang="ts" setup>
import type { GoogleRegistrationFormType } from '@/types/authFormTypes';
import { FormInstance, FormRules } from 'element-plus';
import { inject, reactive, ref } from 'vue';
import { commonRules } from '@/constants/formRules';

const googleRegistrationFormInstance = ref<FormInstance>();

const googleRegistrationFormModel = reactive<GoogleRegistrationFormType>({
  firstName: '',
  lastName: '',
  roomNumber: null,
});

const googleRegistrationFormRules = reactive<FormRules>({
  firstName: [commonRules.required],
  lastName: [commonRules.required],
  roomNumber: [commonRules.room],
});

const handleUserGoogleRegister = inject('handleUserGoogleRegister', async (form: GoogleRegistrationFormType) => {
  console.log('Injection error', form);
});

const handleGoogleRegistrationFormSubmit = async () => {
  if (!googleRegistrationFormInstance.value) return;
  await googleRegistrationFormInstance.value.validate(async (valid) => {
    if (valid) await handleUserGoogleRegister(googleRegistrationFormModel);
  });
};
</script>

<style lang="scss" scoped></style>
