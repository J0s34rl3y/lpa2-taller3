from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UsuarioCreate(BaseModel):
    nombre: str
    correo: EmailStr


class UsuarioRead(UsuarioCreate):
    id: int
    fecha_registro: datetime

    model_config = ConfigDict(from_attributes=True)
