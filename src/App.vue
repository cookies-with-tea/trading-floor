<template>
  <router-view />
  <el-button @click="gg">getself</el-button>
</template>

<script lang="ts" setup>
import { userApi } from '@/api/user/user.api';
import { ElMessage } from 'element-plus';

const gg = async () => {
  const ans = await userApi.getSelf();
  const [error, data] = ans;

  console.log('data: ', data);

  if (data) {
    ElMessage(data.first_name);
  } else {
    ElMessage('error');
  }
};
</script>
