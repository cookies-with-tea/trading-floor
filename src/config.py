from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str
    base_url: str


@dataclass
class Config:
    tgbot: TgBot


def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        tgbot=TgBot(
            token=env.str('BOT_TOKEN'),
            base_url=env.str('BASE_URL'),
        )
    )
