import { AxiosService } from '@/api/AxiosService/axiosService';
import { AxiosRequestConfig } from 'axios';
import { GoogleCredentials } from '@/api/auth/auth.types';
import { GoogleRegistrationFormType } from '@/types/authFormTypes';

class AuthApi extends AxiosService {
  constructor(config: AxiosRequestConfig) {
    super(config);
  }

  authGoogleUser(code: string) {
    return this.axiosCall<GoogleCredentials>({
      method: 'post',
      url: '/google',
      data: {
        authorization_code: code,
      },
    });
  }

  confirmGoogleUser(payload: GoogleRegistrationFormType) {
    return this.axiosCall<GoogleCredentials>({
      method: 'post',
      url: 'sign-up',
      data: {
        first_name: payload.firstName,
        last_name: payload.lastName,
        room_number: payload.roomNumber,
      },
    });
  }

  logout() {
    localStorage.removeItem('accessToken');
  }
}

export const authApi = new AuthApi({
  baseURL: '/api/auth/',
});
