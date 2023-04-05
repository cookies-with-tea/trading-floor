<template>
  <el-input
    ref="inputInstance"
    :disabled="props.disabled"
    :model-value="props.modelValue"
    :placeholder="props.searchable ? props.label : ''"
    data-tid="c-input"
    v-bind="$attrs"
    v-on="$attrs"
    @update:model-value="handleInput"
  />
</template>

<script lang="ts" setup>
import { ElInput } from 'element-plus';
import { CInputType } from '@/components/common/CInput/CInput.type';

type Props = {
  modelValue: string;
  type?: CInputType;
  label?: string;
  disabled?: boolean;
  showPassword?: boolean;
  searchable?: boolean;
};

type Emits = {
  (e: 'update:modelValue', value: string): void;
  (e: 'focus'): void;
  (e: 'blur'): void;
};

const props = withDefaults(defineProps<Props>(), {
  modelValue: '',
  type: 'text',
  label: '',
  disabled: false,
  showPassword: false,
  searchable: false,
});
const emits = defineEmits<Emits>();

const handleInput = (value: string): void => {
  emits('update:modelValue', value);
};
</script>
