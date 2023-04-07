export type Credentials = {
  refresh: string;
  access: string;
};

export type GoogleCredentials = {
  refresh: string;
  access: string;
  isActive: boolean;
};

export type OnlyRefreshCredentials = {
  refresh: string;
};

export type AuthData = {
  email: string;
  password: string;
};
