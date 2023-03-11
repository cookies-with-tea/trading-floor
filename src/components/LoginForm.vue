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
      <div class="d-f jc-sb">
        <router-link :to="{ name: 'registration' }" class="d-b">Регистрация</router-link>
        <el-form-item class="d-f jc-sb">
          <el-button class="d-b" type="primary" @click="submitForm">Войти </el-button>
        </el-form-item>
      </div>
    </el-form>
  </div>
</template>

<script lang="ts" setup>
import type { LoginForm } from '@/types/auth'
import { FormInstance, FormRules } from 'element-plus'
import { reactive, ref } from 'vue'
import { required_field_validation } from '@/validators/common'
import { errorMessage, successMessage } from '@/presets/messages'

const formInstance = ref<FormInstance>()

const formModel = reactive<LoginForm>({
  email: '',
  password: '',
})

const formRules = reactive<FormRules>({
  email: required_field_validation,
  password: required_field_validation,
})

const submitForm = () => {
  if (!formInstance.value) return

  formInstance.value.validate((valid) => {
    if (valid) {
      successMessage()
    } else {
      errorMessage()
    }
  })
}
</script>
