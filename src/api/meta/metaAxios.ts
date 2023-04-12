import { AxiosResponseType } from '@/api/meta/metaAxios.types';
import axios, { AxiosInstance, AxiosRequestConfig } from 'axios';

export class MetaAxios {
  protected axiosInstance!: AxiosInstance;
  constructor(config: AxiosRequestConfig) {
    this.axiosInstance = axios.create(config);
  }
  protected async axiosCall<T = any>(config: AxiosRequestConfig): AxiosResponseType<T> {
    try {
      const { data } = await this.axiosInstance.request<T>(config);

      return [null, data];
    } catch (error: any) {
      console.log(error);

      return [error];
    }
  }
}
