<template>
  <div class="auth-layout">
    <router-view />
  </div>
</template>

<style scoped>
.auth-layout {
  min-height: 100vh;
  max-width: 400px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  border-radius: 20px;
  padding: 20px;
  margin: 0 auto;
}
</style>
