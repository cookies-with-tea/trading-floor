<template>
  <el-button type="primary" @click="isEditContactsDialogVisible = true">Редактировать контакты</el-button>
  <base-dialog v-model="isEditContactsDialogVisible">
    <label for="tg">Тelegram</label>
    <el-input v-model="contacts.tg" name="tg" />
    <label for="vk">Вконтакте</label>
    <el-input v-model="contacts.vk" name="vk" />
    <el-button type="primary" @click="handleContactsChange">Сохранить</el-button>
  </base-dialog>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue';
import { userApi } from '@/api/KY/UserService/user.api';

const isEditContactsDialogVisible = ref(false);

const contacts = reactive({
  vk: '',
  tg: '',
});

const handleContactsChange = async () => {
  const [error] = await userApi.updateSelf({ vk_username: contacts.vk, telegram_username: contacts.tg });

  if (!error) isEditContactsDialogVisible.value = false;
};
</script>

<style lang="scss" scoped></style>
