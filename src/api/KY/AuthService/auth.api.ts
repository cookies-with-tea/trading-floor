import { KyApi } from '@/api/KY/meta/ApiService/ky.api';
import { GoogleAnswer } from '@/api/KY/AuthService/auth.types';
import { GoogleRegistrationFormType } from '@/types/authFormTypes';
import { useTokens } from '@/composables/useTokens';

class AuthApi extends KyApi {
  loginGoogleUser = async (code: string) => {
    return this.kyCall<GoogleAnswer>('google', {
      method: 'post',
      json: { authorization_code: code },
    });
  };

  logoutUser = async () => {
    const { removeRefresh, removeAccess } = useTokens(localStorage);

    removeRefresh();

    removeAccess();
  };

  registerGoogleUser = async (form: GoogleRegistrationFormType) => {
    return this.kyCall<GoogleAnswer>('sign-up', {
      method: 'post',
      json: {
        first_name: form.firstName,
        last_name: form.lastName,
        room_number: form.roomNumber,
      },
    });
  };
}

export const authApi = new AuthApi({
  prefixUrl: '/api/auth',
});
