<template>
  <router-view />
  <el-button @click="gg">getself</el-button>
</template>

<script lang="ts" setup>
import { ElMessage } from 'element-plus';
import { userApi } from '@/api/KY/UserService/user.api';

const gg = async () => {
  const [, data] = await userApi.getSelf();

  if (data) {
    ElMessage(data.first_name);
  } else {
    ElMessage('error');
  }
};
</script>
