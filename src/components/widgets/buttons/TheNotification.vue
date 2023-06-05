<template>
  <button class="notification">
    <icon-template height="21" name="notification" width="18" />
  </button>
</template>

<style lang="scss" scoped>
.notification,
.notification:active {
  max-width: fit-content;
  max-height: fit-content;
  border: none;
  border-radius: 50%;
  color: $color--hint;
  background-color: transparent;
  padding: 5px;
  margin-right: 10px;

  &:hover {
    cursor: pointer;
  }
}
</style>
