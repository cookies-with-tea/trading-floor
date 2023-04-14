import { TokenPair } from '@/api/Axios/token/token.types';

export type GoogleAnswer = TokenPair & {
  is_register: boolean;
};
