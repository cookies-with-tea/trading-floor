import { KyService } from '@/api/KY/meta/KYService/kyService';
import { TokenPairResponse } from '@/api/KY/commonTypes';

class TokenApi extends KyService {
  refreshTokens(refresh: string) {
    return this.kyCall<TokenPairResponse>('refresh', {
      method: 'post',
      json: { refresh },
    });
  }
}

export const tokenApi = new TokenApi({
  prefixUrl: 'api/auth',
});
