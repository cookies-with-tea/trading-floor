import type { FormItemRule } from 'element-plus'
import { required_field_validation } from '@/validators/common'

export const email_validate_rules: FormItemRule[] = [
  required_field_validation,
  // { type: 'email', message: 'Неверный формат почты' }
  // {
  //   pattern: '^[\\w-\\.]+@mer.ci.nsu.ru',
  //   message: 'Почта должна принадлежать доменной сети Высшего Колледжа Информатики'
  // }
]

export const fisrt_name_validate_rules: FormItemRule[] = [
  required_field_validation,
  { pattern: '^[а-яА-Я-]*$', message: 'Имя должно состоять только из букв русского алфавита' },
]

export const last_name_validate_rules: FormItemRule[] = [
  { pattern: '^[а-яА-Я-]*$', message: 'Фамилия должна состоять только из букв русского алфавита' },
]

export const room_number_validate_rules: FormItemRule[] = [
  required_field_validation,
  { type: 'number', message: 'Номер комнаты должен быть числом' },
]

export const password_validate_rules: FormItemRule[] = [
  required_field_validation,
  { min: 8, message: 'Длина пароля должна быть не меньше 8 символов' },
]

// export const username_validate_rules: FormItemRule[] = [
//   { required: true, message: 'Обязательное поле' },
//   { min: 2, message: 'Длина имени должна быть не меньше 2 символов' },
//   {
//     pattern: '^[a-zA-Z0-9а-яА-Я_.-]*$',
//     message: 'Имя может содержать только цифры, буквы русского и латинского алфавита, и _'
//   }
// ]
