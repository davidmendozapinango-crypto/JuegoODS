from dataclasses import dataclass
from typing import Optional


@dataclass
class Player:
    cedula: str
    full_name: str
    sex: str
    birthdate: str
    state_code: str
    access_key: str

    def to_dict(self) -> dict:
        return {
            "cedula": self.cedula,
            "full_name": self.full_name,
            "sex": self.sex,
            "birthdate": self.birthdate,
            "state_code": self.state_code,
            "access_key": self.access_key,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Player":
        return cls(
            cedula=data["cedula"],
            full_name=data["full_name"],
            sex=data["sex"],
            birthdate=data["birthdate"],
            state_code=data["state_code"],
            access_key=data["access_key"],
        )
