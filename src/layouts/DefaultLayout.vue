<template>
  <div class="default-layout">
    <tf-header class="mb-20" />
    <div class="content">
      <div class="container">
        <router-view />
      </div>
    </div>
    <tf-footer />
  </div>
</template>

<script lang="ts" setup>
import TfHeader from '@/components/widgets/TheHeader.vue';
import TfFooter from '@/components/widgets/TheFooter.vue';
</script>

<style lang="scss" scoped>
.content {
  flex: 1 0 auto;
}

.default-layout {
  min-height: 100%;
  display: flex;
  flex-direction: column;
}
</style>
