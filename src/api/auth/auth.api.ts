import { AxiosService } from '@/api/AxiosService/axiosService';
import { AxiosRequestConfig } from 'axios';
import { AuthData, Credentials } from '@/api/auth/auth.types';
import { useAuthStore } from '@/stores/authStore';

class AuthApi extends AxiosService {
  authStore: any;

  constructor(config: AxiosRequestConfig) {
    super(config);

    this.authStore = useAuthStore();
  }

  authUser(payload: AuthData) {
    this.axiosCall<Credentials>({
      method: 'post',
      url: '/token/',
      data: payload,
    }).then((result) => {
      if (result[0] === null) {
        const { refresh, access } = result[1];

        localStorage.setItem('access', access);

        this.authStore.refresh = refresh;

        console.log({ access, refresh });
      } else {
        console.log(result[0]);
      }
    });
  }

  authGoogleUser(payload: string) {
    this.axiosCall<Credentials>({
      method: 'post',
      url: '/google/',
      data: payload,
    }).then((result) => {
      if (result[0] === null) {
        const { refresh, access } = result[1];

        localStorage.setItem('access', access);

        this.authStore.refresh = refresh;

        console.log({ access, refresh });
      }
    });
  }
}

export const authApi = new AuthApi({
  baseURL: '/api/auth/',
});
