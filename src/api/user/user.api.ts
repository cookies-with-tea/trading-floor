import { AxiosService } from '@/api/AxiosService/axiosService';
import { AxiosRequestConfig } from 'axios';
import { UserResponseType } from '@/api/user/user.types';

class UserApi extends AxiosService {
  constructor(config: AxiosRequestConfig) {
    super(config);
  }

  getUser(id: number) {
    return this.axiosCall<UserResponseType>({
      method: 'get',
      url: id.toString(),
    });
  }
  getSelf() {
    console.log('getSelf');

    return this.axiosCall<UserResponseType>({
      method: 'get',
      url: 'me',
    });
  }
}

export const userApi = new UserApi({
  baseURL: '/api/v1/users/',
});
