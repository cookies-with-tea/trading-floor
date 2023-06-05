import { AdvertisementUrgencyEnum, AllowedAdvertisementTypesType } from '@/types/advertisementTypes';
import { UploadFile } from 'element-plus';

export type GoogleRegistrationFormType = {
  firstName: string;
  lastName: string;
  roomNumber: number;
  avatar?: UploadFile;
};

export type AdvertisementCreateFormType = {
  title: string;
  description: string;
  advertisementType: AllowedAdvertisementTypesType;
  images: UploadFile[];
  urgencyType: AdvertisementUrgencyEnum;
  category: number;
};
