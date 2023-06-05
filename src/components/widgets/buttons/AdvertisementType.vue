<template>
  <div :class="advertisementType.toLowerCase()" class="advertisement-type">
    {{ RussianAdvertisementTypeEnum[advertisementType] }}
  </div>
</template>

<script lang="ts" setup>
import { AdvertisementTypeEnum } from '@/types/advertisementTypes';
import { RussianAdvertisementTypeEnum } from '@/components/widgets/AdvertisementPreview/AdvertisementPreview.types';

type Props = {
  advertisementType: AdvertisementTypeEnum;
};

defineProps<Props>();
</script>

<style lang="scss" scoped>
.advertisement-type {
  width: fit-content;
  height: fit-content;
  border-radius: 5px;
  padding: 3px 5px;

  &.buy {
    background-color: #8300004d;
  }

  &.sell {
    background-color: #4bb5434d;
  }

  &.exchange {
    background-color: #c169184d;
  }

  &.take {
    background-color: #00b709;
  }

  &.give {
    background-color: #b79c35;
  }
}
</style>
