from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional


@dataclass(frozen=True)
class Timestamp:
    value : Optional[datetime]

    def __post_init__(self):
        if self.value is None:
            # Se aceptan nullos
            return
        if not isinstance(self.value,datetime):
            raise ValueError(f"The type of the time is incorrect (recive : {type(self.value)}, requires : datetime)")
        now = datetime.now(timezone.utc)
        if self.value > now:
            raise ValueError(f"Timestamp cannot be in the future: {self.value.isoformat()} > {now.isoformat()}")