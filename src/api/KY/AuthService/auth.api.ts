import { KyApi } from '@/api/KY/meta/ApiService/ky.api';
import { GoogleAnswer } from '@/api/KY/AuthService/auth.types';
import { GoogleRegistrationFormType } from '@/types/authFormTypes';
import { STORAGE_ITEMS_NAMES } from '@/constants/storageNames';

class AuthApi extends KyApi {
  loginGoogleUser(code: string) {
    return this.kyCall<GoogleAnswer>('google', {
      method: 'post',
      json: { authorization_code: code },
    });
  }

  logoutUser() {
    localStorage.removeItem(STORAGE_ITEMS_NAMES.accessToken);

    localStorage.removeItem(STORAGE_ITEMS_NAMES.refreshToken);
  }

  registerGoogleUser(form: GoogleRegistrationFormType) {
    return this.kyCall<GoogleAnswer>('sign-up', {
      method: 'post',
      json: {
        first_name: form.firstName,
        last_name: form.lastName,
        room_number: form.roomNumber,
      },
    });
  }
}

export const authApi = new AuthApi({
  prefixUrl: '/api/auth',
});
