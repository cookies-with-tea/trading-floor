def email_normalization(email, logger):
    email = email or ''
    try:
        email_name, domain_part = email.strip().rsplit('@', 1)
    except ValueError:
        logger.error('Incorrect email')
    else:
        if domain_part.lower() != 'mer.ci.nsu.ru':
            raise TypeError('Email must end with a "@mer.ci.nsu.ru"')
        email = f'{email_name}@{domain_part.lower()}'

    return email
