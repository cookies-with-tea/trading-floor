import { FormItemRule } from 'element-plus';

export const RULES_STATUSES: Record<string, string> = {
  required: 'Это поле обязательно для заполнения',
  onlyRussian: 'Это поле должно состоять только из букв русского алфавита',
  passwordLength: 'Длина пароля должна быть не меньше 8 символов',
  domain: 'Почта должна принадлежать домену ВКИ',
  room: 'Номер комнаты должен быть числом',
  email: 'Неверный формат почты',
};

export const commonRules: Record<string, FormItemRule> = {
  required: { required: true, message: RULES_STATUSES.required },
  onlyRussian: { pattern: '^[а-яА-Я-]*$', message: RULES_STATUSES.onlyRussian },
  email: { type: 'email', message: RULES_STATUSES.email },
  domain: { pattern: '^[\\w-\\.]+@mer.ci.nsu.ru', message: RULES_STATUSES.domain },
  passwordLength: { min: 8, message: RULES_STATUSES.passwordLength },
  room: { type: 'number', message: RULES_STATUSES.room },
};
