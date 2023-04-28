import { KyApi } from '@/api/KY/meta/ApiService/ky.api';
import { ApiAdvertisementListType, ApiAdvertisementType } from '@/api/KY/AdvertisementService/advertisement.types';

class AdvertisementApi extends KyApi {
  getAllAdvertisements = async () => {
    return this.kyCall<ApiAdvertisementListType>('', {
      method: 'get',
    });
  };

  getAdvertisement = async (id: number) => {
    return this.kyCall<ApiAdvertisementType>(`/${id}`, {
      method: 'get',
    });
  };
  addAdvertisement = async (advertisement: ApiAdvertisementType) => {
    return this.kyCall<ApiAdvertisementType>('', {
      method: 'post',
      json: advertisement,
    });
  };

  deleteAdvertisement = async (id: number) => {
    return this.kyCall(`/${id}`, {
      method: 'delete',
    });
  };

  updateAdvertisement = async (id: number, advertisement: ApiAdvertisementType) => {
    return this.kyCall<ApiAdvertisementType>(`/${id}`, {
      method: 'patch',
      json: advertisement,
    });
  };
}

export const advertisementApi = new AdvertisementApi({
  prefixUrl: '/api/v1/advertisements',
});
