<template>
  <div class="advertisement-list">
    <advertisement-preview
      v-for="advertisement in advertisements"
      :key="advertisement.id"
      :advertisement="advertisement"
    />
  </div>
</template>

<script lang="ts" setup>
import { ApiAdvertisementListItemType } from '@/api/KY/AdvertisementService/advertisement.types';
import AdvertisementPreview from '@/components/widgets/AdvertisementPreview/AdvertisementPreview.vue';

type Props = {
  advertisements: ApiAdvertisementListItemType[];
};

defineProps<Props>();
</script>

<style lang="scss" scoped>
.advertisement-list {
  display: flex;
  flex-wrap: wrap;
  grid-gap: 10px;
}
</style>
