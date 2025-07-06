from dataclasses import dataclass

@dataclass(frozen=True)
class UserPhotoUrl:
    value : str

    def __post_init__(self):
        if self.value is None:
            return
        if not isinstance(self.value,str):
            raise ValueError(f"The type of the URL is incorrect (recive : {type(self.value)}, requires : str)")
        # Agregar en el futuro validacion del dominio donde esta guardada la imagen (bloop de AZURE, AWS, etc...)