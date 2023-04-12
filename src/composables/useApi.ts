import { ref, watch } from 'vue';
import { AxiosResponseType } from '@/api/meta/metaAxios.types';

export const data = ref<unknown>(null);

const isDataChanged = ref(false);

export const setData = <T = unknown>(newData: T) => {
  data.value = newData;
};

export const useApi = async <T = unknown>(responseData: Awaited<AxiosResponseType<T>>): AxiosResponseType<T> => {
  const [error, response] = responseData;

  if (isDataChanged.value) {
    return [null, data.value as T];
  } else if (!error && response) {
    return [null, response as T];
  }

  return [error as Error];
};

watch(
  () => data.value,
  () => {
    isDataChanged.value = true;
  }
);
