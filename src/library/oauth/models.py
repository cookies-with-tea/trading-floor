from dataclasses import dataclass


@dataclass
class GoogleCredentials:
    authorization_code: str


@dataclass
class GoogleUser:
    email: str
    picture: str
