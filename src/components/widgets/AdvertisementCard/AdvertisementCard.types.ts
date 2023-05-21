enum RussianAdvertisementTypeEnum {
  EXCHANGE = 'Обмен',
  SELL = 'Продажа',
  BUY = 'Покупка',
  GIVE = 'Подарок',
  TAKE = 'Принятие',
}

enum RussianAdvertisementUrgencyEnum {
  urgent = 'Срочно',
  nsu = 'Не очень срочно',
  naau = 'Вообще не срочно',
}

export type AdvertisementCardType = {
  title: string;
  description: string;
  urgency: Array<RussianAdvertisementUrgencyEnum>;
  advertisement_type: Array<RussianAdvertisementTypeEnum>;
  images: Array<string>;
};
