import { AfterResponseHook, BeforeRequestHook } from 'ky';
import { tokenApi } from '@/api/KY/TokenService/token.api';
import { useTokens } from '@/composables/useTokens';
import router from '@/router';

export const requestAuthorizationHeader: BeforeRequestHook = (request: Request) => {
  const { getAccess } = useTokens(localStorage);

  const access = getAccess();

  if (access) {
    request.headers.set('Authorization', `Bearer ${access}`);
  }
};

export const responseRetryOn401: AfterResponseHook = async (request, options, response) => {
  if (response.status === 401) {
    const { getRefresh, setRefresh, setAccess } = useTokens(localStorage);

    const storeRefresh = getRefresh();

    if (storeRefresh) {
      const [error, data] = await tokenApi.refreshTokens(storeRefresh);

      if (!error && data) {
        const { refresh, access } = data;

        setRefresh(refresh);

        setAccess(access);

        request.headers.set('Authorization', `Bearer ${access}`);

        // @ts-ignore
        return this.kyInstance(request);
      }

      await router.push({ name: 'LoginPage' });
    }
  }
};
