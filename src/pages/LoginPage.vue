<template>
  <div class="login-page">
    <div class="d-f jc-c">
      <div>
        <h2 class="ta-c mb-30">Регистрация&nbsp; |&nbsp; Авторизация</h2>
        <google-auth />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup></script>

<style lang="scss" scoped>
.login-page {
  display: flex;
  flex: 1 0;
  flex-direction: column;
  justify-content: center;
}
</style>
