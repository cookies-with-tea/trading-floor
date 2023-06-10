export type ApiUserType = {
  id: number;
  first_name: string;
  last_name: string;
  room_number: number;
  avatar: string;
  avatar_color: string;
  telegram_username: string;
  vk_username: string;
  created_at: string;
  updated_at: string;
  is_active: boolean;
  is_staff: boolean;
  user: string;
};

export type ApiPatchedUserType = {
  avatar?: string;
  first_name?: string;
  last_name?: string;
  telegram_username?: string;
  vk_username?: string;
};
