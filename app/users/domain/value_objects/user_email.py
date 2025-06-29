from dataclasses import dataclass
import re


@dataclass(frozen=True)
class UserEmail:
    value: str

    def __post_init__(self):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, self.value):
            raise ValueError(f"Invalid email: {self.value}")
        local, domain = self.value.split('@',1)

        if len(local) > 64:
            raise ValueError(f"The local is too long : size local = {len(local)} > 64")
        if len(domain) > 243:
            raise ValueError(f"The domain is too long : size domain = {len(domain)} > 244")
        if len(self.value) > 254:
            raise  ValueError(f"The email is too long : size email = {len(self.value)} > 255")