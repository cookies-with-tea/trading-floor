<template>
  <teleport to="#dialogs-container">
    <el-dialog
      ref="dialogRef"
      :model-value="props.modelValue"
      :show-close="false"
      align-center
      class="base-dialog"
      v-bind="$attrs"
      @close="$emit('update:modelValue', false)"
    >
      <el-button>
        <icon-template class="icon-25 base-dialog__close" name="close" @click="handleClose" />
      </el-button>
      <slot />
    </el-dialog>
  </teleport>
</template>

<script lang="ts" setup>
type Props = {
  modelValue: boolean;
};

type Emits = {
  (e: 'update:modelValue', value: boolean): void;
  (e: 'close'): void;
};

const props = defineProps<Props>();

const emits = defineEmits<Emits>();

const handleClose = (): void => {
  emits('update:modelValue', false);

  emits('close');
};
</script>

<style lang="scss" scoped>
.base-dialog {
  position: relative;

  .el-button {
    top: -15px;
    right: -15px;
    width: 50px;
    height: 50px;
    position: absolute;
    border-radius: 50%;
    background-color: $color--box-secondary;
  }
}
</style>
