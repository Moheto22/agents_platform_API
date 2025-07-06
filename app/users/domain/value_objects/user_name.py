from  dataclasses import dataclass
from typing import re


@dataclass(frozen=True)
class UserName:
    value: str

    def __post_init__(self):
        if not self.value.isalpha():
            raise ValueError("The value name is not alpha")
        if len(self.value) > 20:
            raise  ValueError(f"Name too long: {len(self.value)} > 20")

