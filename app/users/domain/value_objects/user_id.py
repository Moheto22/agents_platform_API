from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class UserId:
    value:Optional[int]

    def __post_init__(self):
        if self.value is None:
            return
        if not isinstance(self.value,int):
            raise ValueError(f"The type of the id is incorrect (recive : {type(self.value)}, required : int")
