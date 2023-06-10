<template>
  <button class="notification">
    <icon-template class="icon-44" name="profile" />
  </button>
</template>

<script lang="ts" setup></script>

<style lang="scss" scoped>
.notification {
  color: $color--header-text;

  &:hover {
    cursor: pointer;
  }
}
</style>
