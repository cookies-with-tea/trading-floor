from typing import Optional


def str_to_int(number: str) -> Optional[int]:
    try:
        number: int = int(number)
    except ValueError:
        return

    return number
