import re
from dataclasses import dataclass

@dataclass(frozen=True)
class UserTenant:
    value : str

    def __post_init__(self):
        if not isinstance(self.value,str):
            raise ValueError(f"The type of the tenant is incorrect (recive : {type(self.value)}, requires : str)")
        if not self.value.isalpha():
            raise ValueError("The tenant value is not alpha")
        if not re.fullmatch("^[a-z0-9_]+$",self.value):
            raise ValueError("Tenant must contain only lowercase letters, numbers, and underscores")
