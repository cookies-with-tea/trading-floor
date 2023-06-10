import { AdvertisementTypeEnum, AdvertisementUrgencyEnum } from '@/types/advertisementTypes';
import { ApiUserType } from '@/api/KY/UserService/user.types';

export type ApiAdvertisementImageType = {
  id: number;
  url: string;
};

export type ApiAdvertisementCategoryType = {
  id: number;
  title: string;
};

export type ApiAdvertisementType = {
  id: number;
  title: string;
  description: string;
  advertisement_type: AdvertisementTypeEnum[];
  images: ApiAdvertisementImageType[];
  urgency_type: AdvertisementUrgencyEnum;
  category: ApiAdvertisementCategoryType;
  is_open: boolean;
  author: ApiUserType;
};

export type ApiAllAdvertisementQueryParams = {
  author__id?: number;
  category?: number;
  is_open?: boolean;
};

export type ApiAdvertisementListType = {
  count: number;
  prev: string;
  next: string;
  results: ApiAdvertisementListItemType[];
};

export type ApiAdvertisementListItemType = {
  id: number;
  title: string;
  description: string;
  advertisement_type: AdvertisementTypeEnum[];
  images: ApiAdvertisementImageType[];
  urgency_type: AdvertisementUrgencyEnum;
  category: ApiAdvertisementCategoryType;
  is_open: boolean;
  author: ApiUserType;
};

export type ApiPatchedAdvertisementType = {
  id?: number;
  title?: string;
  description?: string;
  advertisement_type?: AdvertisementTypeEnum[];
  images?: ApiAdvertisementImageType[];
  urgency_type?: AdvertisementUrgencyEnum;
  category?: ApiAdvertisementCategoryType;
  is_open?: boolean;
};
