<template>
  <div class="user-card d-f fd-c jc-sb ai-c">
    <el-image :src="avatar" class="user-card__avatar" />
    <div class="user-card__name">
      <span> {{ firstName }} {{ lastName }} </span>
    </div>
  </div>
</template>

<script lang="ts" setup>
type Props = {
  avatar: string;
  firstName: string;
  lastName: string;
};

defineProps<Props>();
</script>

<style lang="scss" scoped>
.user-card {
  width: 160px;
  height: 205px;
  flex: 0 0 auto;
  background-color: $color--box;
  padding: 5px;

  &__name {
  }

  &__avatar {
    width: 90px;
    height: 90px;
    border-radius: 50%;
    margin: 0 auto;
    margin-bottom: 5px;
  }
}
</style>
