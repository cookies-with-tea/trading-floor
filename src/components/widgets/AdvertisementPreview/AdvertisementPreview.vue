<template>
  <div class="advertisement-preview">
    <div class="advertisement-preview__image">
      <el-image :src="advertisement.images[0].url" fit="cover" />
    </div>

    <div class="advertisement-preview__info">
      <div>
        <div class="advertisement-preview__title">
          <p>{{ advertisement.title }}</p>
        </div>
        <div class="advertisement-preview__description">
          <p>{{ advertisement.description }}</p>
        </div>
      </div>
      <div class="advertisement-preview__types">
        <advertisement-type v-for="type in advertisement.advertisement_type" :key="type" :advertisement-type="type" />
      </div>
    </div>
    <el-button class="advertisement-preview__response-button" type="primary">Откликнуться</el-button>
    <el-button class="advertisement-preview__goto-button" type="primary"> Перейти к объявлению </el-button>
  </div>
</template>

<script lang="ts" setup>
import { ApiAdvertisementListItemType } from '@/api/KY/AdvertisementService/advertisement.types';

defineProps<{
  advertisement: ApiAdvertisementListItemType;
}>();
</script>

<style lang="scss" scoped>
.advertisement-preview {
  display: grid;
  grid-gap: 10px;
  grid-template-columns: 160px 278px;
  grid-template-rows: 120px 24px;
  border-radius: 5px;
  font-size: 12px;
  background-color: $color--field;
  padding: 10px;

  &__title {
    justify-self: start;
    font-size: 14px;
    white-space: nowrap;
    text-overflow: ellipsis;
    margin-bottom: 29px;
    overflow: hidden;
  }

  &__description {
    display: -webkit-box;
    line-height: 14.06px;
    word-break: break-word;
    margin-bottom: 10px;
    overflow: hidden;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
  }

  &__types {
    justify-self: end;
  }

  &__image {
    grid-column-start: 1;
    grid-row-start: 1;

    .el-image {
      width: 160px;
      height: 120px;
      border-radius: 5px;
    }
  }

  &__info {
    max-height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    grid-column-start: 2;
    grid-row: 1;
    font-size: 12px;
  }

  :deep(.el-button) {
    height: 24px;
    display: flex;
    font-size: inherit;
    background-color: $color--primary-light;
    padding: 0;
    margin: 0;
  }

  &__goto-button {
    grid-column-start: 2;
    grid-row-start: 2;
  }

  &__response-button {
    grid-column-start: 1;
    grid-row-start: 2;
  }
}
</style>
