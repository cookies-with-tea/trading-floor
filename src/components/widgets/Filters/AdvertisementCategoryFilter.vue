<template>
  <el-checkbox-group v-model="selectedCategories" class="category-filter">
    <el-checkbox
      v-for="category in allCategories"
      :key="category.id"
      :label="category.id"
      @change="handleCheckBoxChange"
    >
      {{ category.title }}
    </el-checkbox>
  </el-checkbox-group>
</template>

<script lang="ts" setup>
import { inject, Ref, ref, watch } from 'vue';
import { ApiAdvertisementCategoryType } from '@/api/KY/AdvertisementService/advertisement.types';

type Props = {
  isReset: boolean;
};

type Emits = {
  (e: 'update:isReset', value: boolean): void;
};

const props = defineProps<Props>();
const emits = defineEmits<Emits>();

const selectedCategories = inject<Ref<number[]>>('selectedCategories', ref([]));
const allCategories = inject<Ref<ApiAdvertisementCategoryType[]>>('allCategories', ref([]));

const handleCheckBoxChange = async () => {
  emits('update:isReset', false);
};

watch(
  () => props.isReset,
  (newIsReset) => {
    if (newIsReset) {
      selectedCategories.value = [];
    }
  }
);
</script>

<style lang="scss" scoped>
.category-filter {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  row-gap: 10px;
}
</style>
