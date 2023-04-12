import { AxiosRequestConfig } from 'axios';
import { ElMessage } from 'element-plus';
import { MetaAxios } from '@/api/meta/metaAxios';
import { MESSAGES } from '@/constants/messages';
import { tokenApi } from '@/api/token/token.api';
import { setData } from '@/composables/useApi';

export class AxiosService extends MetaAxios {
  constructor(config: AxiosRequestConfig) {
    super(config);

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
      async (error: any) => {
        const response = error?.response?.data;

        switch (error?.response?.status) {
          case 401:
            if (error?.response?.data?.messages[0].message === MESSAGES.TOKEN_EXPIRED) {
              const refreshToken = localStorage.getItem('refreshToken');

              if (refreshToken) {
                const [response_error, data] = await tokenApi.refreshTokens(refreshToken);

                if (!response_error && data) {
                  localStorage.setItem('accessToken', data.access);

                  localStorage.setItem('refreshToken', data.refresh);

                  const [newError, newData] = await this.axiosCall(error.config);

                  if (!newError && newData) {
                    setData(newData);
                  }
                }
              }
            }

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
}
