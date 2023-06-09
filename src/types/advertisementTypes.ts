export enum AdvertisementTypeEnum {
  exchange = 'EXCHANGE',
  sell = 'SELL',
  buy = 'BUY',
  give = 'GIVE',
  take = 'TAKE',
}

export const AllAdvertisementTypes = [
  AdvertisementTypeEnum.sell,
  AdvertisementTypeEnum.exchange,
  AdvertisementTypeEnum.take,
  AdvertisementTypeEnum.buy,
  AdvertisementTypeEnum.give,
];

export enum AdvertisementUrgencyEnum {
  urgent = 'URGENT',
  nsu = 'NSU',
  naau = 'NAAU',
}

export type AllowedAdvertisementTypesType =
  | [AdvertisementTypeEnum.exchange, AdvertisementTypeEnum.sell]
  | [AdvertisementTypeEnum.exchange, AdvertisementTypeEnum.take]
  | [AdvertisementTypeEnum.take, AdvertisementTypeEnum.buy, AdvertisementTypeEnum.exchange]
  | [AdvertisementTypeEnum.sell, AdvertisementTypeEnum.give, AdvertisementTypeEnum.exchange];

export const AllowedAdvertisementTypes = [
  [AdvertisementTypeEnum.exchange, AdvertisementTypeEnum.sell],
  [AdvertisementTypeEnum.exchange, AdvertisementTypeEnum.take],
  [AdvertisementTypeEnum.take, AdvertisementTypeEnum.buy, AdvertisementTypeEnum.exchange],
  [AdvertisementTypeEnum.sell, AdvertisementTypeEnum.give, AdvertisementTypeEnum.exchange],
];
