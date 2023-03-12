from utils.strings import is_correct_email_domain


def test_is_correct_email_domain() -> None:
    assert is_correct_email_domain('testemail@gmail.com', '@gmail.com')
    assert not is_correct_email_domain('testemail@gmail.com', '@mail.com')

    assert is_correct_email_domain('testemail@mer.ci.nsu.ru', '@mer.ci.nsu.ru')
    assert not is_correct_email_domain('testemail@mer.ci.nsu.com', '@mer.ci.nsu.ru')
