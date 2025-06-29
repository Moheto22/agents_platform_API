from dataclasses import dataclass

@dataclass(frozen=True)
class UserId:
    value:int

    def __post_init__(self):
        if not isinstance(self.value,int):
            raise ValueError(f"The type of the id is incorrect (recive : {type(self.value)}, required : int")
