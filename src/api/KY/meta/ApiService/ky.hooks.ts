import { AfterResponseHook, BeforeRequestHook } from 'ky';
import { tokenApi } from '@/api/KY/TokenService/token.api';

export const requestAuthorizationHeader: BeforeRequestHook = (request: Request) => {
  const token = localStorage.getItem('accessToken');

  if (token) {
    request.headers.set('Authorization', `Bearer ${token}`);
  }
};

export const responseRetryOn401: AfterResponseHook = async (request, options, response) => {
  if (response.status === 401) {
    const refresh = localStorage.getItem('refreshToken');

    if (refresh) {
      const [error, data] = await tokenApi.refreshTokens(refresh);

      if (!error && data) {
        const { refresh, access } = data;

        localStorage.setItem('refreshToken', refresh);

        localStorage.setItem('accessToken', access);

        request.headers.set('Authorization', `Bearer ${access}`);

        // @ts-ignore
        return this.kyInstance(request);
      }
    }
  }
};
