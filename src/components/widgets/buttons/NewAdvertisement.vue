<template>
  <el-button class="new-advertisement" type="primary" @click="handleNewAdvertisementButtonClick">
    Новое объявление
  </el-button>
  <base-dialog v-model="isNewAdvertisementDialogVisible">
    <h2 class="ta-c">Новое объявление</h2>
    <create-advertisement-form class="mt-30" @created="handleCreate" />
  </base-dialog>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import CreateAdvertisementForm from '@/components/Forms/CreateAdvertisementForm.vue';

const isNewAdvertisementDialogVisible = ref(false);

const handleNewAdvertisementButtonClick = async () => {
  isNewAdvertisementDialogVisible.value = true;
};

const handleCreate = async () => {
  isNewAdvertisementDialogVisible.value = false;

  location.reload();
};
</script>

<style lang="scss" scoped>
.new-advertisement {
  width: 100%;
  height: 100%;
  max-width: 160px;
  max-height: 36px;
}
</style>
