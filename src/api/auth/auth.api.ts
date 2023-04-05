import { AxiosService } from '@/api/AxiosService/axiosService';
import { AxiosRequestConfig } from 'axios';
import { AuthData, Credentials } from '@/api/auth/auth.types';

class AuthApi extends AxiosService {
  constructor(config: AxiosRequestConfig) {
    super(config);
  }

  authUser(payload: AuthData) {
    return this.axiosCall<Credentials>({
      method: 'post',
      url: '/token/',
      data: payload,
    });
  }

  authGoogleUser(code: string) {
    return this.axiosCall<Credentials>({
      method: 'post',
      url: '/google/',
      data: {
        authorization_code: code,
      },
    });
  }
}

export const authApi = new AuthApi({
  baseURL: '/api/auth/',
});
