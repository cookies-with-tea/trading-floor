import { ApiTokenPairType } from '@/api/KY/commonTypes';

export type ApiGoogleAnswerType = ApiTokenPairType & {
  is_register: boolean;
};

export type ApiGoogleRegistrationFormType = {
  first_name: string;
  last_name: string;
  room_number: number;
  avatar?: File;
};
