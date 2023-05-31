<template>
  <div class="categories-sidebar">
    <el-button class="category--all" type="primary" @click="changeCategory(null)">Все объявления</el-button>
    <hr class="color-hovered-button" />
    <el-button
      v-for="category in categories"
      :key="category.id"
      :class="{ 'category--selected': current == category.id }"
      class="category"
      type="primary"
      @click="changeCategory(category.id)"
    >
      {{ category.title }}
    </el-button>
  </div>
</template>

<script lang="ts" setup>
import { ApiAdvertisementCategoryType } from '@/api/KY/AdvertisementService/advertisement.types';
import { onBeforeMount, ref } from 'vue';
import { advertisementApi } from '@/api/KY/AdvertisementService/advertisement.api';

type Props = {
  modelValue: number | null;
};

type Emits = {
  (e: 'update:modelValue', value: number | null): void;
};

const props = defineProps<Props>();

const emits = defineEmits<Emits>();

const categories = ref<ApiAdvertisementCategoryType[]>([]);

const current = ref(props.modelValue);

const changeCategory = async (value: number | null) => {
  current.value = value;

  emits('update:modelValue', value);
};

onBeforeMount(async () => {
  const [error, data] = await advertisementApi.getAllCategories();

  if (!error && data) {
    categories.value = data;
  }
});
</script>

<style lang="scss" scoped>
@mixin category {
  width: 182px;
  height: 42px;
  max-width: 182px;
  border-radius: 3px;
  font-size: 12px;
  white-space: normal;
  text-align: left;
  background-color: $color--box;
  padding: 5px 10px;
  margin: 0;
}

.categories-sidebar {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border-radius: 5px;
  background-color: $color--box;
  padding: 15px;
  row-gap: 10px;

  .category {
    @include category;

    &--selected,
    &:hover {
      background-color: $color--field;
    }

    &--all {
      color: #648cf2;
      background-color: $color--field;
      padding: 10px 5px;
    }
  }
}
</style>
