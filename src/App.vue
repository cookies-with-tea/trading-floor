<template>
  <router-view />
  <el-button @click="gg">getself</el-button>
</template>

<script lang="ts" setup>
import { ElMessage } from 'element-plus';
import { useApi } from '@/composables/useApi';
import { userApi } from '@/api/user/user.api';
import { UserResponseType } from '@/api/user/user.types';

const gg = async () => {
  const [error, data] = await useApi<UserResponseType>(await userApi.getSelf());

  console.log('data: ', data);

  if (data) {
    ElMessage(data.first_name);
  } else {
    ElMessage('error');
  }
};
</script>
