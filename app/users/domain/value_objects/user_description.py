from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class UserDescription:
    value : Optional[str]

    def __post_init__(self):
        if self.value is None:
            # Se aceptan nullos
            return
        if not isinstance(self.value,str) and self.value != None:
            raise ValueError(f"The type of the description is incorrect (recive : {type(self.value)}, requires : str)")
        if len(self.value) > 500:
            raise ValueError(f"The description is too long : size description = {len(self.value)} > 500")