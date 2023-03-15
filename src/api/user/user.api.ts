import { AxiosService } from '@/api/AxiosService/axiosService';
import { AxiosRequestConfig } from 'axios';
import { RegisterFormType } from '@/types/auth';

class UserApi extends AxiosService {
  constructor(config: AxiosRequestConfig) {
    super(config);
  }

  registerUser(payload: RegisterFormType) {
    return this.axiosCall({
      method: 'post',
      url: '',
      data: payload,
    });
  }
}

export const userApi = new UserApi({
  baseURL: '/api/v1/users/',
});
