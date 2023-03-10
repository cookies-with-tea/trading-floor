export type LoginForm = {
  email: string;
  password: string;
};

export type RegisterForm = {
  email: string;
  first_name: string;
  last_name?: string;
  password: string;
  room_number: number | null;
};
