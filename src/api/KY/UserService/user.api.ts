import { KyApi } from '@/api/KY/meta/ApiService/ky.api';
import { UserResponse } from '@/api/KY/UserService/user.types';

class UserApi extends KyApi {
  getSelf() {
    return this.kyCall<UserResponse>('me', {
      method: 'get',
    });
  }
  getUser(id: number) {
    return this.kyCall<UserResponse>(`${id}`, {
      method: 'get',
    });
  }
}

export const userApi = new UserApi({
  prefixUrl: '/api/v1/users',
});
