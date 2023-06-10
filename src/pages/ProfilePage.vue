<template>
  <div class="profile-page">
    <div>
      <user-card :avatar="user.avatar" :first-name="user.first_name" :last-name="user.last_name" class="mb-20" />
      <edit-contacts />
    </div>

    <div class="profile-page__body">
      <h2 class="mb-15">Объявления пользователя</h2>
      <el-switch v-model="isActiveAdvertisement" active-text="Открытые" inactive-text="Закрытые" />
      <advertisement-list :advertisements="advertisements" :self-user-id="user.id" />
    </div>
  </div>
</template>

<script lang="ts" setup>
import UserCard from '@/components/widgets/UserCard.vue';
import { computed, onBeforeMount, reactive, ref } from 'vue';
import { ApiUserType } from '@/api/KY/UserService/user.types';
import { userApi } from '@/api/KY/UserService/user.api';
import { advertisementApi } from '@/api/KY/AdvertisementService/advertisement.api';
import { ApiAdvertisementListItemType } from '@/api/KY/AdvertisementService/advertisement.types';

const user = reactive<ApiUserType>({
  id: 0,
  first_name: '',
  last_name: '',
  room_number: 0,
  avatar: '',
  created_at: '',
  updated_at: '',
  is_active: false,
  is_staff: false,
  user: '',
  vk_username: '',
  telegram_username: '',
  avatar_color: '',
});

const allLoadedUserAdvertisements = ref<ApiAdvertisementListItemType[]>([]);

const isActiveAdvertisement = ref(true);

const loadUser = async () => {
  const [error, data] = await userApi.getSelf();

  if (!error && data) {
    Object.assign(user, data);
  }
};

const loadUserAdvertisements = async () => {
  const [error, data] = await advertisementApi.getAllAdvertisements({ author__id: user.id });

  if (!error && data) {
    allLoadedUserAdvertisements.value = data.results;
  }
};

const advertisements = computed(() =>
  allLoadedUserAdvertisements.value.filter((el) => el.is_open === isActiveAdvertisement.value)
);

onBeforeMount(async () => {
  await loadUser();

  await loadUserAdvertisements();
});
</script>

<style lang="scss" scoped>
.profile-page {
  display: flex;
  column-gap: 72px;
  justify-content: space-between;
}
</style>
