<template>
  <div class="home-page">
    <div class="home-page__title">
      <h2>Последние объявления</h2>
    </div>
    <div class="home-page__categories">
      <categories-sidebar v-model="selectedCategory" class="mb-20" />
      <new-advertisement />
    </div>
    <div class="home-page__advertisements">
      <advertisement-list :advertisements="advertisements" />
    </div>
  </div>
</template>

<script lang="ts" setup>
import AdvertisementList from '@/components/widgets/AdvertisementList.vue';
import CategoriesSidebar from '@/components/widgets/CategoriesSidebar.vue';
import { computed, onBeforeMount, ref } from 'vue';
import { advertisementApi } from '@/api/KY/AdvertisementService/advertisement.api';
import { ApiAdvertisementListItemType } from '@/api/KY/AdvertisementService/advertisement.types';

const selectedCategory = ref<number | null>(null);

const loadedAdvertisement = ref<Array<ApiAdvertisementListItemType>>([]);

const loadAdvertisements = async () => {
  const [error, data] = await advertisementApi.getAllAdvertisements();

  if (!error && data) {
    loadedAdvertisement.value = data;
  }
};

onBeforeMount(loadAdvertisements);

const advertisements = computed(() => {
  return loadedAdvertisement.value.filter(
    (el) => selectedCategory.value == null || el.category.id == selectedCategory.value
  );
});
</script>

<style lang="scss" scoped>
.home-page {
  display: grid;
  grid-gap: 20px;

  &__categories {
    grid-column-start: 1;
    grid-row-start: 2;
  }

  &__title {
    grid-column-start: 2;
    grid-row-start: 1;
  }

  &__advertisements {
    grid-column-start: 2;
    grid-row-start: 2;
  }
}
</style>
