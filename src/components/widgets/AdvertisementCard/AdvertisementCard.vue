<template>
  <div class="advertisement-card">
    <div class="advertisement-card--image-section">
      <img :src="props.images[0]" alt="дед инсайд" />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { AdvertisementCardType } from '@/components/widgets/AdvertisementCard/AdvertisementCard.types';

const props = defineProps<AdvertisementCardType>();
</script>

<style lang="scss" scoped>
.advertisement-card {
  padding: 10px;
}
</style>
