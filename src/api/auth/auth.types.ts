export type Credentials = {
  refresh: string;
  access: string;
};

export interface OnlyRefreshCredentials {
  refresh: string;
}

export interface AuthData {
  email: string;
  password: string;
}
