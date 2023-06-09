<template>
  <el-checkbox-group v-model="selectedTypes" class="type-filter">
    <el-checkbox
      v-for="(type, index) in AllAdvertisementTypes"
      :key="type"
      :label="index"
      @change="handleCheckBoxChange"
    >
      {{ RussianAdvertisementTypeEnum[type] }}
    </el-checkbox>
  </el-checkbox-group>
</template>

<script lang="ts" setup>
import { inject, Ref, ref, watch } from 'vue';
import { AllAdvertisementTypes } from '@/types/advertisementTypes';
import { RussianAdvertisementTypeEnum } from '../AdvertisementPreview/AdvertisementPreview.types';

type Props = {
  isReset: boolean;
};

type Emits = {
  (e: 'update:isReset', value: boolean): void;
};

const props = defineProps<Props>();
const emits = defineEmits<Emits>();

const selectedTypes = inject<Ref<number[]>>('selectedTypes', ref([]));

const handleCheckBoxChange = async () => {
  emits('update:isReset', false);
};

watch(
  () => props.isReset,
  (newIsReset) => {
    if (newIsReset) {
      selectedTypes.value = [];
    }
  }
);
</script>

<style lang="scss" scoped>
.type-filter {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  row-gap: 10px;
}
</style>
