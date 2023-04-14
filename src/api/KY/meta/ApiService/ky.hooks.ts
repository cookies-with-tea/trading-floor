import { AfterResponseHook, BeforeRequestHook } from 'ky';
import { tokenApi } from '@/api/KY/TokenService/token.api';
import { STORAGE_ITEMS_NAMES } from '@/constants/storageNames';

export const requestAuthorizationHeader: BeforeRequestHook = (request: Request) => {
  const token = localStorage.getItem(STORAGE_ITEMS_NAMES.accessToken);

  if (token) {
    request.headers.set('Authorization', `Bearer ${token}`);
  }
};

export const responseRetryOn401: AfterResponseHook = async (request, options, response) => {
  if (response.status === 401) {
    const refresh = localStorage.getItem(STORAGE_ITEMS_NAMES.refreshToken);

    if (refresh) {
      const [error, data] = await tokenApi.refreshTokens(refresh);

      if (!error && data) {
        const { refresh, access } = data;

        localStorage.setItem(STORAGE_ITEMS_NAMES.refreshToken, refresh);

        localStorage.setItem(STORAGE_ITEMS_NAMES.accessToken, access);

        request.headers.set('Authorization', `Bearer ${access}`);

        // @ts-ignore
        return this.kyInstance(request);
      }
    }
  }
};
