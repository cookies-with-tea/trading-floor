import ky, { Options } from 'ky';
import { KyInstance } from 'ky/distribution/types/ky';
import { KyResponseType } from '@/api/KY/meta/KYService/kyService.types';

export class KyService {
  protected kyInstance!: KyInstance;

  constructor(options: Options) {
    this.kyInstance = ky.create(options);
  }
  protected kyCall = async <T = any>(url: string, options: Options): KyResponseType<T> => {
    try {
      const data = await this.kyInstance(url, options).json<T>();

      return [null, data];
    } catch (e: any) {
      return [e];
    }
  };
}
