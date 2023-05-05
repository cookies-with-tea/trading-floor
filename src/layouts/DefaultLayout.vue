<template>
  <div class="default-layout">
    <header class="bg-header">
      <div class="container jc-sb">
        <icon-template height="55" name="vki" width="160" />
        <div class="d-f ai-c">
          <icon-template class="mr-10" height="21" name="notification" width="18" />
          <icon-template class="icon-44" name="profile" />
        </div>
      </div>
    </header>
    <div class="content">
      <div class="container">
        <router-view />
      </div>
    </div>
    <footer class="bg-footer">
      <div class="container" />
    </footer>
  </div>
</template>

<script lang="ts" setup></script>

<style lang="scss" scoped>
footer {
  min-height: 43px;
}

.content {
  flex: 1 0 auto;
}

.default-layout {
  min-height: 100%;
  display: flex;
  flex-direction: column;
}
</style>
