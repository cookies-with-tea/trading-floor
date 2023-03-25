import axios, { AxiosInstance, AxiosRequestConfig } from 'axios';
import { AxiosResponseType } from '@/api/AxiosService/axiosService.types';
import { ElMessage } from 'element-plus';

export class AxiosService {
  private axiosInstance!: AxiosInstance;

  constructor(config: AxiosRequestConfig) {
    this.axiosInstance = axios.create(config);

    this.axiosInstance.interceptors.request.use((config: AxiosRequestConfig) => {
      const token = localStorage.getItem('accessToken');

      if (token) {
        config.headers = {
          Authorization: `Bearer ${token}`,
        };
      }

      return config;
    });

    this.axiosInstance.interceptors.response.use(
      (response: any) => {
        const status = response?.status;

        switch (status) {
          case 201:
            ElMessage({
              type: 'success',
              message: response?.data?.message,
            });
        }

        return Promise.resolve(response);
      },
      (error: any) => {
        const response = error?.response?.data;

        switch (error?.response?.status) {
          case 401:
            break;
          case 403:
            break;
          case 404:
            break;
          case 422:
            break;
          case 500:
            ElMessage({
              type: 'error',
              message: response.message,
            });
        }

        return Promise.reject(response);
      }
    );
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
