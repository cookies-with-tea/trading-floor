<template>
  <div>
    <header class="bg-header">
      <div class="container jc-sb">
        <icon-template height="55" name="vki" width="160" />
        <div class="d-f ai-c">
          <the-notification />
          <profile-icon />
        </div>
      </div>
    </header>
  </div>
</template>

<script lang="ts" setup>
import TheNotification from '@/components/widgets/buttons/TheNotification.vue';
import ProfileIcon from '@/components/widgets/buttons/ProfileIcon.vue';
</script>
