<template>
  <header class="bg-header">
    <div class="container jc-sb">
      <icon-template
        class="vki-icon"
        height="55"
        name="vki"
        width="160"
        @click="$router.push({ name: ROUTE_NAMES.HomePage })"
      />
      <div class="d-f ai-c">
        <el-image
          :src="avatar"
          class="profile-icon mr-20"
          @click="$router.push({ name: ROUTE_NAMES.ProfilePage, params: { id: userId } })"
        />
        <new-advertisement />
      </div>
    </div>
  </header>
</template>

<script lang="ts" setup>
import { userApi } from '@/api/KY/UserService/user.api';
import { onBeforeMount, ref } from 'vue';
import { ROUTE_NAMES } from '@/constants/routeNames';

const userId = ref(0);
const avatar = ref('');

const loadUserId = async () => {
  const [error, data] = await userApi.getSelf();

  if (!error && data) {
    userId.value = data.id;

    avatar.value = data.avatar;
  }
};

onBeforeMount(loadUserId);
</script>

<style lang="scss" scoped>
.vki-icon {
  &:hover {
    cursor: pointer;
  }
}

.profile-icon {
  width: 44px;
  height: 44px;
  min-width: 44px;
  min-height: 44px;
  flex: 1 1 auto;
  border-radius: 50%;

  &:hover {
    cursor: pointer;
  }
}
</style>
