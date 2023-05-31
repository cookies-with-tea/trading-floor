<template>
  <el-form
    ref="createAdvertisementFormInstance"
    :model="createAdvertisementFormModel"
    :rules="createAdvertisementFormRules"
  >
    <el-form-item prop="title">
      <label for="title">Название</label>
      <el-input v-model="createAdvertisementFormModel.title" name="title" placeholder="Заголовок" />
    </el-form-item>
    <el-form-item prop="description">
      <label for="description">Описание</label>
      <el-input
        v-model="createAdvertisementFormModel.description"
        name="description"
        placeholder="Описание"
        type="textarea"
      />
    </el-form-item>
    <el-form-item prop="urgencyType">
      <label for="urgency">Срочность</label>
      <el-radio-group v-model="createAdvertisementFormModel.urgencyType" name="urgency">
        <el-radio v-for="urgency in AdvertisementUrgencyEnum" :key="urgency" :label="urgency">{{
          RussianAdvertisementUrgencyEnum[urgency]
        }}</el-radio>
      </el-radio-group>
    </el-form-item>
    <label for="category">Категория</label>
    <el-form-item prop="category">
      <el-select v-model="createAdvertisementFormModel.category">
        <el-option v-for="category in categories" :key="category.id" :label="category.title" :value="category.id" />
      </el-select>
    </el-form-item>
    <label for="type">Тип объявления</label>
    <el-form-item prop="advertisementType">
      <el-select v-model="createAdvertisementFormModel.advertisementType" default-first-option name="type" remote>
        <el-option v-for="option in typesOption" :key="option.key" :label="option.label" :value="option.value" />
      </el-select>
    </el-form-item>
    <label for="images">Добавьте изображения</label>
    <el-form-item prop="images">
      <el-upload
        v-model:file-list="createAdvertisementFormModel.images"
        :auto-upload="false"
        :limit="10"
        action=""
        drag
        list-type="picture-card"
        multiple
        name="images"
      >
        <el-button>Загрузить</el-button>
      </el-upload>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="handleCreateAdvertisementFormSubmit">Создать</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import { onBeforeMount, reactive, ref } from 'vue';
import { ElMessage, FormInstance, FormRules, UploadFile } from 'element-plus';
import { commonRules } from '@/constants/formRules';
import { AdvertisementCreateFormType } from '@/types/formTypes';
import { AdvertisementTypeEnum, AdvertisementUrgencyEnum, AllowedAdvertisementTypes } from '@/types/advertisementTypes';
import { advertisementApi } from '@/api/KY/AdvertisementService/advertisement.api';
import { ApiAdvertisementCategoryType } from '@/api/KY/AdvertisementService/advertisement.types';
import {
  RussianAdvertisementTypeEnum,
  RussianAdvertisementUrgencyEnum,
} from '@/components/widgets/AdvertisementPreview/AdvertisementPreview.types';

type Emits = {
  (e: 'created'): void;
};

const emits = defineEmits<Emits>();

const createAdvertisementFormInstance = ref<FormInstance>();

const createAdvertisementFormModel = reactive<AdvertisementCreateFormType>({
  title: '',
  description: '',
  category: 1,
  urgencyType: AdvertisementUrgencyEnum.nsu,
  advertisementType: [AdvertisementTypeEnum.exchange, AdvertisementTypeEnum.sell],
  images: [],
});

const createAdvertisementFormRules = reactive<FormRules>({
  title: [commonRules.required],
  description: [commonRules.required],
  category: [commonRules.required],
  urgencyType: [commonRules.required],
  advertisementType: [commonRules.required],
  images: [commonRules.required],
});

const handleCreateAdvertisementFormSubmit = async (): Promise<void> => {
  if (!createAdvertisementFormInstance.value) return;

  await createAdvertisementFormInstance.value.validate(async (valid) => {
    if (valid) {
      const formData = new FormData();

      formData.append('title', createAdvertisementFormModel.title);

      formData.append('description', createAdvertisementFormModel.description);

      createAdvertisementFormModel.advertisementType.forEach((type: AdvertisementTypeEnum) => {
        formData.append('advertisement_type', type);
      });

      createAdvertisementFormModel.images.forEach((image: UploadFile) => {
        if (image.raw) formData.append('images', image.raw);
      });

      formData.append('urgency_type', createAdvertisementFormModel.urgencyType);

      formData.append('category', createAdvertisementFormModel.category.toString());

      const [error] = await advertisementApi.addAdvertisement(formData);

      if (!error) {
        return emits('created');
      } else {
        ElMessage('Failed');
      }
    }
  });
};

const categories = ref<ApiAdvertisementCategoryType[]>([]);

const typesOption = AllowedAdvertisementTypes.map((type) => ({
  value: type,
  label: type.map((el) => RussianAdvertisementTypeEnum[el]).join('/'),
  key: type.toString(),
}));

onBeforeMount(async () => {
  const [error, data] = await advertisementApi.getAllCategories();

  if (!error && data) {
    categories.value = data;
  }
});
</script>

<style lang="scss" scoped></style>
