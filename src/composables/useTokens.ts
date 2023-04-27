import { STORAGE_ITEMS_NAMES } from '@/constants/storageNames';

export const useTokens = (storage: Storage) => {
  const getAccess = (): string | null => {
    return storage.getItem(STORAGE_ITEMS_NAMES.accessToken);
  };

  const getRefresh = (): string | null => {
    return storage.getItem(STORAGE_ITEMS_NAMES.refreshToken);
  };

  const setAccess = (token: string): void => {
    storage.setItem(STORAGE_ITEMS_NAMES.accessToken, token);
  };

  const setRefresh = (token: string): void => {
    storage.setItem(STORAGE_ITEMS_NAMES.refreshToken, token);
  };

  const removeAccess = (): void => {
    storage.removeItem(STORAGE_ITEMS_NAMES.accessToken);
  };

  const removeRefresh = (): void => {
    storage.removeItem(STORAGE_ITEMS_NAMES.refreshToken);
  };

  return { getAccess, getRefresh, setAccess, setRefresh, removeAccess, removeRefresh };
};
