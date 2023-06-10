import { KyApi } from '@/api/KY/meta/ApiService/ky.api';
import {
  ApiAdvertisementCategoryType,
  ApiAdvertisementListType,
  ApiAdvertisementType,
  ApiAllAdvertisementQueryParams,
  ApiPatchedAdvertisementType,
} from '@/api/KY/AdvertisementService/advertisement.types';

class AdvertisementApi extends KyApi {
  getAllAdvertisements = async (params?: ApiAllAdvertisementQueryParams) => {
    return await this.kyCall<ApiAdvertisementListType>('', {
      method: 'get',
      searchParams: params,
    });
  };

  getAdvertisement = async (id: number) => {
    return await this.kyCall<ApiAdvertisementType>(`${id}`, {
      method: 'get',
    });
  };
  addAdvertisement = async (advertisement: FormData) => {
    return await this.kyCall<ApiAdvertisementType>('', {
      method: 'post',
      body: advertisement,
    });
  };

  deleteAdvertisement = async (id: number) => {
    return await this.kyCall(`${id}`, {
      method: 'delete',
    });
  };

  updateAdvertisement = async (id: number, advertisement: ApiPatchedAdvertisementType) => {
    return await this.kyCall<ApiAdvertisementType>(`${id}/`, {
      method: 'patch',
      json: advertisement,
    });
  };

  getAllCategories = async () => {
    return await this.kyCall<ApiAdvertisementCategoryType[]>('categories', {
      method: 'get',
    });
  };
}

export const advertisementApi = new AdvertisementApi({
  prefixUrl: '/api/v1/advertisements',
});
