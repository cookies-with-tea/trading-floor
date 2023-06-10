<template>
  <div class="advertisement-list">
    <advertisement-preview
      v-for="advertisement in advertisements"
      :key="advertisement.id"
      :advertisement="advertisement"
      :is-own="selfUserId == advertisement.author.id"
      @deleted="handleDelete"
    />
  </div>
</template>

<script lang="ts" setup>
import { ApiAdvertisementListItemType } from '@/api/KY/AdvertisementService/advertisement.types';
import AdvertisementPreview from '@/components/widgets/AdvertisementPreview/AdvertisementPreview.vue';

type Emits = {
  (e: 'delete', value: number): void;
};

type Props = {
  advertisements: ApiAdvertisementListItemType[];
  selfUserId: number;
};

defineProps<Props>();

const emits = defineEmits<Emits>();

const handleDelete = (value: number) => {
  emits('delete', value);
};
</script>

<style lang="scss" scoped>
.advertisement-list {
  display: flex;
  flex-wrap: wrap;
  grid-gap: 10px;
}
</style>
