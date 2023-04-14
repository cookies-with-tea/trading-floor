import { TokenPairResponse } from '@/api/KY/commonTypes';

export type GoogleAnswer = TokenPairResponse & {
  is_register: boolean;
};
