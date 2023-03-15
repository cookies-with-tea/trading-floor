export type LoginFormType = {
  email: string;
  password: string;
};

export type RegisterFormType = {
  email: string;
  first_name: string;
  last_name?: string;
  password: string;
  room_number: number | null;
};
