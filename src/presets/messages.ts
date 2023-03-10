import { ElMessage } from 'element-plus';

export const successMessage = () =>
  ElMessage({
    message: 'Удачно',
    type: 'success'
  });

export const errorMessage = () =>
  ElMessage({
    message: 'Что-то не так',
    type: 'error'
  });
