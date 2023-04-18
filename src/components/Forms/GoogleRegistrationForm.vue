<template>
  <el-form
    ref="googleRegistrationFormInstance"
    :model="googleRegistrationFormModel"
    :rules="googleRegistrationFormRules"
  >
    <el-form-item prop="firstName">
      <label for="name">Имя</label>
      <el-input v-model="googleRegistrationFormModel.firstName" name="name" placeholder="your gender" />
    </el-form-item>
    <el-form-item prop="lastName">
      <label for="lastName">Фамилия</label>
      <el-input v-model="googleRegistrationFormModel.lastName" name="lastName" placeholder="racial identity" />
    </el-form-item>
    <el-form-item prop="roomNumber">
      <label for="room">№ Комнаты</label>
      <el-input v-model.number="googleRegistrationFormModel.roomNumber" name="room" placeholder="sex" />
    </el-form-item>
    <el-button type="primary" @click="handleGoogleRegistrationFormSubmit">Зарегистрироваться</el-button>
  </el-form>
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
  roomNumber: [commonRules.room, commonRules.required],
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

<style lang="scss" scoped>
.form {
}
</style>
