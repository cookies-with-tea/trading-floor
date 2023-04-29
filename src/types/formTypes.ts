import { AdvertisementUrgencyEnum, AllowedAdvertisementTypesType } from '@/types/advertisementTypes';

export type GoogleRegistrationFormType = {
  firstName: string;
  lastName: string;
  roomNumber: number;
  avatar?: File;
};

export type AdvertisementCreateFormType = {
  title: string;
  description: string;
  advertisementType: AllowedAdvertisementTypesType;
  images?: Array<File>;
  urgencyType: AdvertisementUrgencyEnum;
  category: number;
};
