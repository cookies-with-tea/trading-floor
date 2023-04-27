import { KyApi } from '@/api/KY/meta/ApiService/ky.api';
import { UserResponse } from '@/api/KY/UserService/user.types';

class UserApi extends KyApi {
  getSelf = async () => {
    return this.kyCall<UserResponse>('me', {
      method: 'get',
    });
  };
  getUser = async (id: number) => {
    return this.kyCall<UserResponse>(`${id}`, {
      method: 'get',
    });
  };
}

export const userApi = new UserApi({
  prefixUrl: '/api/v1/users',
});
