export type Credentials = {
  refresh: string;
  access: string;
};

export type OnlyRefreshCredentials = {
  refresh: string;
};

export type AuthData = {
  email: string;
  password: string;
};
