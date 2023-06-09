<template>
  <div class="home-page">
    <div class="home-page__title">
      <h2>Последние объявления</h2>
    </div>
    <div class="home-page__categories">
      <filters-sidebar class="mb-20" />
    </div>
    <div class="home-page__advertisements">
      <advertisement-list :advertisements="advertisements" />
    </div>
  </div>
</template>

<script lang="ts" setup>
import AdvertisementList from '@/components/widgets/AdvertisementList.vue';
import { computed, onBeforeMount, provide, ref } from 'vue';
import { advertisementApi } from '@/api/KY/AdvertisementService/advertisement.api';
import {
  ApiAdvertisementCategoryType,
  ApiAdvertisementListItemType,
} from '@/api/KY/AdvertisementService/advertisement.types';
import { AdvertisementUrgencyEnum, AllAdvertisementTypes } from '@/types/advertisementTypes';

const selectedCategories = ref<number[]>([]);
const allCategories = ref<ApiAdvertisementCategoryType[]>([]);

const loadedAdvertisement = ref<ApiAdvertisementListItemType[]>([]);

const selectedUrgencies = ref<AdvertisementUrgencyEnum[]>([]);

const selectedTypes = ref<number[]>([]);

const loadAdvertisements = async () => {
  const [error, data] = await advertisementApi.getAllAdvertisements();

  if (!error && data) {
    loadedAdvertisement.value = data;
  }
};

const loadCategories = async () => {
  const [error, data] = await advertisementApi.getAllCategories();

  if (!error && data) {
    allCategories.value = data;
  }
};

onBeforeMount(async () => {
  await loadCategories();

  await loadAdvertisements();
});

const advertisements = computed(() => {
  return loadedAdvertisement.value.filter((el) => {
    return (
      (selectedCategories.value.length === 0 || selectedCategories.value.includes(el.category.id)) &&
      (selectedUrgencies.value.length === 0 || selectedUrgencies.value.includes(el.urgency_type)) &&
      (selectedTypes.value.length === 0 ||
        selectedTypes.value
          .map((type_index) => el.advertisement_type.includes(AllAdvertisementTypes[type_index]))
          .some((el) => el))
    );
  });
});

provide('selectedCategories', selectedCategories);

provide('allCategories', allCategories);

provide('selectedUrgencies', selectedUrgencies);

provide('selectedTypes', selectedTypes);
</script>

<style lang="scss" scoped>
.home-page {
  display: grid;
  grid-gap: 20px;
  grid-template-columns: 212px 958px;

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
