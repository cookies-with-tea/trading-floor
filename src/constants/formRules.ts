import type { FormItemRule } from 'element-plus';

export const requiredRule: FormItemRule = {
  required: true,
  message: 'Обязательное поле',
};

export const emailRules: FormItemRule[] = [
  { type: 'email', message: 'Неверный формат почты' },
  {
    pattern: '^[\\w-\\.]+@mer.ci.nsu.ru',
    message: 'Почта должна принадлежать доменной сети Высшего Колледжа Информатики',
  },
];

export const firstNameRules: FormItemRule[] = [
  { pattern: '^[а-яА-Я-]*$', message: 'Имя должно состоять только из букв русского алфавита' },
];

export const lastNameRules: FormItemRule[] = [
  { pattern: '^[а-яА-Я-]*$', message: 'Фамилия должна состоять только из букв русского алфавита' },
];

export const roomNumberRules: FormItemRule[] = [{ type: 'number', message: 'Номер комнаты должен быть числом' }];

export const passwordRules: FormItemRule[] = [{ min: 8, message: 'Длина пароля должна быть не меньше 8 символов' }];
