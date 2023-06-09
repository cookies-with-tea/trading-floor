<template>
  <el-checkbox-group v-model="selectedUrgencies" class="urgency-filter">
    <el-checkbox
      v-for="urgency in AdvertisementUrgencyEnum"
      :key="urgency"
      :label="urgency"
      @change="handleCheckBoxChange"
    >
      {{ RussianAdvertisementUrgencyEnum[urgency] }}
    </el-checkbox>
  </el-checkbox-group>
</template>

<script lang="ts" setup>
import { inject, ref, watch } from 'vue';
import { AdvertisementUrgencyEnum } from '@/types/advertisementTypes';
import { RussianAdvertisementUrgencyEnum } from '../AdvertisementPreview/AdvertisementPreview.types';

type Props = {
  isReset: boolean;
};

type Emits = {
  (e: 'update:isReset', value: boolean): void;
};

const props = defineProps<Props>();
const emits = defineEmits<Emits>();

const selectedUrgencies = inject('selectedUrgencies', ref([]));

const handleCheckBoxChange = async () => {
  emits('update:isReset', false);
};

watch(
  () => props.isReset,
  (newIsReset) => {
    if (newIsReset) {
      selectedUrgencies.value = [];
    }
  }
);
</script>

<style lang="scss" scoped>
.urgency-filter {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  row-gap: 10px;
}
</style>
