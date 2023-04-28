export enum ApiAdvertisementTypeEnum {
  exchange = 'EXCHANGE',
  sell = 'SELL',
  buy = 'BUY',
  give = 'GIVE',
  take = 'TAKE',
}

export type ApiAdvertisementImageType = {
  url: string;
};

export enum ApiAdvertisementUrgencyEnum {
  urgent = 'URGENT',
  nsu = 'NSU',
  naau = 'NAAU',
}

export type ApiAdvertisementCategoryType = {
  id: number;
  title: string;
};

export type ApiAdvertisementType = {
  title: string;
  description: string;
  advertisement_type: Array<ApiAdvertisementTypeEnum>;
  images: Array<ApiAdvertisementImageType>;
  urgency_type: ApiAdvertisementUrgencyEnum;
  category: ApiAdvertisementCategoryType;
};

export type ApiAdvertisementListType = Array<{
  title: string;
  advertisement_type: Array<ApiAdvertisementTypeEnum>;
  urgency_type: ApiAdvertisementUrgencyEnum;
  category: ApiAdvertisementCategoryType;
}>;
