import { ApiTokenPairType } from '@/api/KY/commonTypes';

export type ApiGoogleAnswerType = ApiTokenPairType & {
  is_register: boolean;
};
