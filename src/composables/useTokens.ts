import { STORAGE_ITEMS_NAMES } from '@/constants/storageNames';

export const useTokens = (storage: Storage) => {
  const getAccess = () => {
    return storage.getItem(STORAGE_ITEMS_NAMES.accessToken);
  };

  const getRefresh = () => {
    return storage.getItem(STORAGE_ITEMS_NAMES.refreshToken);
  };

  const setAccess = (token: string) => {
    localStorage.setItem(STORAGE_ITEMS_NAMES.accessToken, token);
  };

  const setRefresh = (token: string) => {
    localStorage.setItem(STORAGE_ITEMS_NAMES.refreshToken, token);
  };

  const removeAccess = () => {
    localStorage.removeItem(STORAGE_ITEMS_NAMES.accessToken);
  };

  const removeRefresh = () => {
    localStorage.removeItem(STORAGE_ITEMS_NAMES.refreshToken);
  };

  return { getAccess, getRefresh, setAccess, setRefresh, removeAccess, removeRefresh };
};
