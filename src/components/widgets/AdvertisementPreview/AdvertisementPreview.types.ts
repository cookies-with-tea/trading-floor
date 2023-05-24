export enum RussianAdvertisementTypeEnum {
  EXCHANGE = 'Обмен',
  SELL = 'Продажа',
  BUY = 'Покупка',
  GIVE = 'Подарок',
  TAKE = 'Принятие',
}

export enum RussianAdvertisementUrgencyEnum {
  URGENT = 'Срочно',
  NSU = 'Не очень срочно',
  NAAU = 'Вообще не срочно',
}

export type AdvertisementCardType = {
  title: string;
  urgency: Array<RussianAdvertisementUrgencyEnum>;
  advertisement_type: Array<RussianAdvertisementTypeEnum>;
  category: number;
};
