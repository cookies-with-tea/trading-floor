import random


def generate_random_color() -> str:
    return f'#{hex(random.randrange(0, 2**24))}'
