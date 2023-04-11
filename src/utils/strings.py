def is_correct_email_domain(email: str, email_domain: str) -> bool:
    return email.endswith(email_domain)
