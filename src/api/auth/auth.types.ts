export type Credentials = {
  refresh: string;
  access: string;
};

export type GoogleCredentials = {
  refresh: string;
  access: string;
  is_register: boolean;
};

export type OnlyRefreshCredentials = {
  refresh: string;
};

export type AuthData = {
  email: string;
  password: string;
};
