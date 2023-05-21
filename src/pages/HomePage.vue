<template>
  <div class="home-page">
    <div class="home-page--body">
      <h2> Последние объявления </h2>
      <new-advertisement />
    </div>
  </div>
</template>

<script lang="ts" setup>
import NewAdvertisement from '@/components/widgets/buttons/NewAdvertisement.vue';
</script>

<style lang="scss" scoped>
.home-page {
  position: relative;
  display: flex;

  &--body {
    flex: 1 1 auto;
  }
}
</style>
