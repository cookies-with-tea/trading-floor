import { AdvertisementTypeEnum, AdvertisementUrgencyEnum } from '@/types/advertisementTypes';

export type ApiAdvertisementImageType = {
  url: string;
};

export type ApiAdvertisementCategoryType = {
  id: number;
  title: string;
};

export type ApiAdvertisementType = {
  title: string;
  description: string;
  advertisement_type: Array<AdvertisementTypeEnum>;
  images: Array<ApiAdvertisementImageType>;
  urgency_type: AdvertisementUrgencyEnum;
  category: ApiAdvertisementCategoryType;
};

export type ApiAdvertisementListItemType = {
  title: string;
  advertisement_type: Array<AdvertisementTypeEnum>;
  urgency_type: AdvertisementUrgencyEnum;
  category: ApiAdvertisementCategoryType;
};

export type ApiPatchedAdvertisementType = {
  title?: string;
  description?: string;
  advertisement_type?: Array<AdvertisementTypeEnum>;
  images?: Array<ApiAdvertisementImageType>;
  urgency_type?: AdvertisementUrgencyEnum;
  category?: ApiAdvertisementCategoryType;
};

export type ApiCreatedAdvertisementType = {
  title: string;
  description: string;
  advertisement_type: Array<AdvertisementTypeEnum>;
  images?: Array<File>;
  urgency_type: AdvertisementUrgencyEnum;
  category: number;
};
