import { MetaAxios } from '@/api/meta/metaAxios';
import { TokenPair } from '@/api/token/token.types';
import { AxiosRequestConfig } from 'axios';

export class TokenApi extends MetaAxios {
  constructor(config: AxiosRequestConfig) {
    super(config);
  }
  refreshTokens(refresh: string) {
    return this.axiosCall<TokenPair>({
      method: 'post',
      url: '/refresh',
      data: { refresh },
    });
  }
}

export const tokenApi = new TokenApi({
  baseURL: 'api/auth',
});
