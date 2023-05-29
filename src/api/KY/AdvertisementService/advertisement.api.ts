import { KyApi } from '@/api/KY/meta/ApiService/ky.api';
import {
  ApiAdvertisementCategoryType,
  ApiAdvertisementListItemType,
  ApiAdvertisementType,
  ApiPatchedAdvertisementType,
} from '@/api/KY/AdvertisementService/advertisement.types';

class AdvertisementApi extends KyApi {
  getAllAdvertisements = async () => {
    return this.kyCall<Array<ApiAdvertisementListItemType>>('', {
      method: 'get',
    });
  };

  getAdvertisement = async (id: number) => {
    return this.kyCall<ApiAdvertisementType>(`${id}`, {
      method: 'get',
    });
  };
  addAdvertisement = async (advertisement: FormData) => {
    return this.kyCall<ApiAdvertisementType>('', {
      method: 'post',
      body: advertisement,
    });
  };

  deleteAdvertisement = async (id: number) => {
    return this.kyCall(`${id}`, {
      method: 'delete',
    });
  };

  updateAdvertisement = async (id: number, advertisement: ApiPatchedAdvertisementType) => {
    return this.kyCall<ApiAdvertisementType>(`${id}`, {
      method: 'patch',
      json: advertisement,
    });
  };

  getAllCategories = async () => {
    return this.kyCall<Array<ApiAdvertisementCategoryType>>('categories', {
      method: 'get',
    });
  };
}

export const advertisementApi = new AdvertisementApi({
  prefixUrl: '/api/v1/advertisements',
});
