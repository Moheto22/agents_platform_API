from  dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class UserRol:
    value: Optional[int]

    def __post_init__(self):
        if self.value is None:
            return
        if 0 > self.value:
            raise  ValueError(f"The id_rol coudn't be negative: {self.value}")
