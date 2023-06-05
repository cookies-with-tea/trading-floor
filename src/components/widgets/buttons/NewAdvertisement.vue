<template>
  <el-button type="primary" @click="handleNewAdvertisementButtonClick"> Новое объявление </el-button>
  <base-dialog v-model="isNewAdvertisementDialogVisible">
    <h2 class="ta-c">Новое объявление</h2>
    <create-advertisement-form class="mt-30" @created="isNewAdvertisementDialogVisible = false" />
  </base-dialog>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import CreateAdvertisementForm from '@/components/Forms/CreateAdvertisementForm.vue';

const isNewAdvertisementDialogVisible = ref(false);

const handleNewAdvertisementButtonClick = async () => {
  isNewAdvertisementDialogVisible.value = true;
};
</script>

<style lang="scss" scoped></style>
