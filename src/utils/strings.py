PERMISSIBLE_ADVERTISEMENT_TYPE = (
    ('Обмен'),
    ('Продам'),
    ('Куплю'),
    ('Отдам'),
    ('Возьму'),
    ('Обмен', 'Продам'),
    ('Обмен', 'Куплю'),
    ('Обмен', 'Отдам'),
    ('Обмен', 'Возьму'),
    ('Продам', 'Отдам'),
    ('Куплю', 'Возьму'),
    ('Обмен', 'Продам', 'Отдам'),
    ('Обмен', 'Куплю', 'Возьму'),
)


def is_correct_email_domain(email: str, email_domain: str) -> bool:
    return email.endswith(email_domain)
