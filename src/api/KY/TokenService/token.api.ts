import { KyService } from '@/api/KY/meta/KYService/kyService';
import { ApiTokenPairType } from '@/api/KY/commonTypes';

class TokenApi extends KyService {
  refreshTokens = async (refresh: string) => {
    return this.kyCall<ApiTokenPairType>('refresh', {
      method: 'post',
      json: { refresh },
    });
  };
}

export const tokenApi = new TokenApi({
  prefixUrl: 'api/auth',
});
