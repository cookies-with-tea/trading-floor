import { KyApi } from '@/api/KY/meta/ApiService/ky.api';
import { GoogleAnswer } from '@/api/KY/AuthService/auth.types';
import { GoogleRegistrationFormType } from '@/types/authFormTypes';

class AuthApi extends KyApi {
  loginGoogleUser(code: string) {
    return this.kyCall<GoogleAnswer>('google', {
      method: 'post',
      json: { authorization_code: code },
    });
  }

  logoutUser() {
    localStorage.removeItem('accessToken');

    localStorage.removeItem('refreshToken');
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
