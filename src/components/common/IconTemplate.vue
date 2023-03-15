<template>
  <svg :class="iconClass" :height="props.height" :width="props.width" aria-hidden="true" class="app-icon">
    <use :href="symbolId" />
  </svg>
</template>

<script lang="ts" setup>
import { computed } from 'vue';

type Props = {
  name: string;
  prefix?: string;
  width?: string | number;
  height?: string | number;
  reverse?: boolean;
};

const props = withDefaults(defineProps<Props>(), {
  prefix: 'icon',
  width: '23px',
  height: '24px',
  reverse: false,
});

const symbolId = computed(() => `#${props.prefix}-${props.name}`);

const iconClass = computed(() => {
  return [{ 'reversed-icon': props.reverse }, `app-icon--${props.name}`];
});
</script>

<style scoped>
.app-icon {
  position: relative;
  display: inline-block;
  flex-shrink: 0;
  transition: transform 0.2s;
}

.reversed-icon {
  transform: rotate(180deg);
}
</style>
