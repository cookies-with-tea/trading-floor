<template>
  <div class="advertisement-preview">
    <h2 class="mb-18"> {{ advertisement.title }} </h2>
    <el-button class="bg-header mb-18" disabled type="primary">{{ advertisement.category.title }}</el-button>
    <div class="d-f">
      <el-button disabled type="primary">{{
        advertisement.advertisement_type.map((el) => RussianAdvertisementTypeEnum[el]).join(', ')
      }}</el-button>
      <el-button disabled type="primary">{{ RussianAdvertisementUrgencyEnum[advertisement.urgency_type] }}</el-button>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ApiAdvertisementListItemType } from '@/api/KY/AdvertisementService/advertisement.types';
import { RussianAdvertisementTypeEnum, RussianAdvertisementUrgencyEnum } from './AdvertisementPreview.types';

const props = defineProps<{
  advertisement: ApiAdvertisementListItemType;
}>();
</script>

<style lang="scss" scoped>
.advertisement-preview {
  border-radius: 5px;
  background-color: $color--field;
  padding: 10px;

  &__image-section {
    width: 160px;
    height: 120px;
  }
}
</style>
