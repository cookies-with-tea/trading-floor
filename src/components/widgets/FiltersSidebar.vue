<template>
  <div class="filters-sidebar">
    <el-button class="reset-button mb-10" type="primary" @click="reset = true">Сбросить фильтры</el-button>
    <hr class="color-hovered-button" />
    <el-collapse class="filters-sidebar__filters-collapse">
      <el-collapse-item title="Категория">
        <advertisement-category-filter v-model:is-reset="reset" />
      </el-collapse-item>
      <el-collapse-item title="Срочность">
        <advertisement-urgency-filter v-model:is-reset="reset" />
      </el-collapse-item>
      <el-collapse-item title="Тип">
        <advertisement-type-filter v-model:is-reset="reset" />
      </el-collapse-item>
    </el-collapse>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import AdvertisementCategoryFilter from '@/components/widgets/Filters/AdvertisementCategoryFilter.vue';
import AdvertisementUrgencyFilter from '@/components/widgets/Filters/AdvertisementUrgencyFilter.vue';
import AdvertisementTypeFilter from '@/components/widgets/Filters/AdvertisementTypeFilter.vue';

const reset = ref(true);
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

.filters-sidebar {
  border-radius: 5px;
  background-color: $color--box;
  padding: 15px;

  .reset-button {
    @include category;

    color: #648cf2;
    background-color: $color--field;
    padding: 10px 5px;
  }

  &__filters-collapse {
    :deep(.el-collapse-item__header) {
    }

    :deep(.el-collapse-item__arrow) {
      margin: 0 auto 0 0;
    }
  }
}
</style>
