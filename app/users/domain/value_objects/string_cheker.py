from dataclasses import dataclass

@dataclass(frozen=True)
class UserStringData:
    value : str

    def __post_init__(self):
        if not isinstance(self.value,str):
            raise ValueError(f"The type of the value is incorrect (recive : {type(self.value)}, requires : str)")