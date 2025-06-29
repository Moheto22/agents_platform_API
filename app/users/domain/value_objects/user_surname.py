from  dataclasses import dataclass
import re

@dataclass(frozen=True)
class UserSurname:
    value: str

    def __post_init__(self):
        if len(self.value) > 40:
            raise  ValueError(f"Surname too long: {len(self.value)} > 40")
        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚÑáéíóúñ\s\-]+", self.value):
            raise ValueError("Surname must contain only letters, spaces or hyphens")