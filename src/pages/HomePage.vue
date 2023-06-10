<template>
  <div class="home-page">
    <div class="home-page__title">
      <h2>Последние объявления</h2>
    </div>
    <div class="home-page__categories">
      <filters-sidebar class="mb-20" />
    </div>
    <div class="home-page__advertisements">
      <advertisement-list :advertisements="advertisements" :self-user-id="userId" @delete="handleAdvertisementClose" />
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
import { userApi } from '@/api/KY/UserService/user.api';

const selectedCategories = ref<number[]>([]);
const allCategories = ref<ApiAdvertisementCategoryType[]>([]);

const loadedAdvertisements = ref<ApiAdvertisementListItemType[]>([]);

const selectedUrgencies = ref<AdvertisementUrgencyEnum[]>([]);

const selectedTypes = ref<number[]>([]);

const userId = ref(0);

const loadAdvertisements = async () => {
  const [error, data] = await advertisementApi.getAllAdvertisements({ is_open: true });

  if (!error && data) {
    loadedAdvertisements.value = data.results;
  }
};

const handleAdvertisementClose = (id: number) => {
  loadedAdvertisements.value = loadedAdvertisements.value.filter((el) => el.id != id);

  console.log(loadedAdvertisements.value);
};

const loadCategories = async () => {
  const [error, data] = await advertisementApi.getAllCategories();

  if (!error && data) {
    allCategories.value = data;
  }
};

const loadUserId = async () => {
  const [error, data] = await userApi.getSelf();

  if (!error && data) {
    userId.value = data.id;
  }
};

onBeforeMount(async () => {
  await loadCategories();

  await loadAdvertisements();

  await loadUserId();
});

const advertisements = computed(() => {
  return loadedAdvertisements.value.filter((el) => {
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
