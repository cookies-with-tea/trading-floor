import { KyApi } from '@/api/KY/meta/ApiService/ky.api';
import { ApiGoogleAnswerType, ApiGoogleRegistrationFormType } from '@/api/KY/AuthService/auth.types';
import { useTokens } from '@/composables/useTokens';

class AuthApi extends KyApi {
  loginGoogleUser = async (code: string) => {
    return this.kyCall<ApiGoogleAnswerType>('google', {
      method: 'post',
      json: { authorization_code: code },
    });
  };

  logoutUser = async () => {
    const { removeRefresh, removeAccess } = useTokens(localStorage);

    removeRefresh();

    removeAccess();
  };

  registerGoogleUser = async (form: ApiGoogleRegistrationFormType) => {
    return this.kyCall<ApiGoogleAnswerType>('sign-up', {
      method: 'post',
      json: form,
    });
  };
}

export const authApi = new AuthApi({
  prefixUrl: '/api/auth',
});
