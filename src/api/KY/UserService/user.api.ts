import { KyApi } from '@/api/KY/meta/ApiService/ky.api';
import { ApiPatchedUserType, ApiUserType } from '@/api/KY/UserService/user.types';

class UserApi extends KyApi {
  getSelf = async () => {
    return await this.kyCall<ApiUserType>('me', {
      method: 'get',
    });
  };

  updateSelf = async (user: ApiPatchedUserType) => {
    return await this.kyCall<ApiPatchedUserType>('me', {
      method: 'patch',
      json: user,
    });
  };
  getUser = async (id: number) => {
    return await this.kyCall<ApiUserType>(`${id}`, {
      method: 'get',
    });
  };
}

export const userApi = new UserApi({
  prefixUrl: '/api/v1/users',
});
