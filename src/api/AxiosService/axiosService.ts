import axios, { AxiosInstance, AxiosRequestConfig } from 'axios';
import { AxiosResponseType } from '@/api/AxiosService/axiosService.types';

export class AxiosService {
  private axiosInstance!: AxiosInstance;

  constructor(config: AxiosRequestConfig) {
    this.axiosInstance = axios.create(config);

    this.axiosInstance.interceptors.request.use((config: AxiosRequestConfig) => {
      const token = localStorage.getItem('token');

      if (token) {
        config.headers = {
          Authorization: `Bearer ${token}`,
        };
      }

      return config;
    });
  }

  protected async axiosCall<T = any>(config: AxiosRequestConfig): AxiosResponseType<T> {
    try {
      const { data } = await this.axiosInstance.request<T>(config);

      return [null, data];
    } catch (error: any) {
      return [error];
    }
  }
}
