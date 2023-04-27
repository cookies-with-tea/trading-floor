import { KyService } from '@/api/KY/meta/KYService/kyService';
import { Options } from 'ky';
import { requestAuthorizationHeader, responseRetryOn401 } from '@/api/KY/meta/ApiService/ky.hooks';

export class KyApi extends KyService {
  constructor(options: Options) {
    options.hooks = {
      beforeRequest: [requestAuthorizationHeader],
      afterResponse: [responseRetryOn401],
    };

    super(options);
  }
}
